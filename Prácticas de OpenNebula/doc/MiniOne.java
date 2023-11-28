import org.opennebula.client.Client;
import org.opennebula.client.OneResponse;
import org.opennebula.client.template.Template;

public class MiniOne {

    public static void main(String[] args) {
        try {
            Client oneClient = new Client("oneadmin:feUTFIfOou", null);
            Template ttyLinux = new Template(2, oneClient);
            OneResponse response = ttyLinux.instantiate("nueva-maquina");
            System.out.println("El id de la nueva máquina instanciada es: " + response.getMessage());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

}
