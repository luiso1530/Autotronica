package com.thenewmotion.ocpp.json.api

import java.net.URI
import com.thenewmotion.ocpp.messages._
import scala.concurrent.Future
import javax.net.ssl.SSLContext

abstract class OcppJsonClient(
  chargerId: String,
  centralSystemUri: URI,
  authPassword: Option[String])(implicit sslContext: SSLContext = SSLContext.getDefault)
  extends OcppEndpoint[CentralSystemReq, CentralSystemRes, ChargePointReq, ChargePointRes] {

  private[this] val ocppStack = new ChargePointOcppConnectionComponent with DefaultSrpcComponent with SimpleClientWebSocketComponent {
    val webSocketConnection = new SimpleClientWebSocketConnection(
      chargerId,
      centralSystemUri,
      authPassword
    )
    val srpcConnection = new DefaultSrpcConnection
    val ocppConnection = new ChargePointOcppConnection

    override def onRequest(req: ChargePointReq): Future[ChargePointRes] =
      OcppJsonClient.this.onRequest(req)

    override def onOcppError(error: OcppError): Unit = OcppJsonClient.this.onError(error)

    override def onDisconnect(): Unit = OcppJsonClient.this.onDisconnect
  }

  def send[REQ <: CentralSystemReq, RES <: CentralSystemRes](req: REQ)(implicit reqRes: ReqRes[REQ, RES]): Future[RES] =
    ocppStack.ocppConnection.sendRequest(req)

  def close() = ocppStack.webSocketConnection.close()
}
