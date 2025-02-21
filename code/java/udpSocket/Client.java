package udpSocket;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Client {
	DatagramSocket client = null;
	DatagramPacket rPacket = null, sPacket = null;

    public void comunica() {
        try {
	        client = new DatagramSocket(4568);
	        byte[] bonin = "bonin   ".getBytes();
	        sPacket = new DatagramPacket(bonin, bonin.length, InetAddress.getLocalHost(), 4567);
	        client.send(sPacket);
	        rPacket = new DatagramPacket(new byte[5], 5);
	        client.receive(rPacket);
	        System.out.println(new String(rPacket.getData(), StandardCharsets.UTF_8));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}