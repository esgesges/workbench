package udpSocket;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Server {
	DatagramSocket server = null;
	DatagramPacket rPacket = null, sPacket = null;

	public void comunica() {
		try {
			server = new DatagramSocket(4567);
			rPacket = new DatagramPacket(new byte[5], 5);
			server.receive(rPacket);
			System.out.println(new String(rPacket.getData(), StandardCharsets.UTF_8));
			sPacket = new DatagramPacket(rPacket.getData(), rPacket.getLength(), rPacket.getAddress(), rPacket.getPort());
			server.send(sPacket);
		} catch (Exception e) {
			System.err.println("errore connessione");
		}
	}
}