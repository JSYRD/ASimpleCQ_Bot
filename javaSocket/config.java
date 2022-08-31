import java.net.MalformedURLException;
import java.net.URL;
import java.net.http.*;
public final class config {
    public static URL listenServer;
    public config() throws MalformedURLException{
        listenServer = new URL("http://127.0.0.1:5701");
        
    }
}
