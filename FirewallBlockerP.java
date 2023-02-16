package Default;

public class FirewallBlockerP extends BlocksUpdater
{
  // Properties
    private boolean enabled;
    private String[] blocked;
  // Contructors
    public FirewallBlockerP(String[] block)
    {
        blocked = block
    }

    public FirewallBlockerP(String[] block, boolean ena)
    {
        blocked = block;
        enabled = ena;
    }
  // Methods
    public static void enable()
    {
        /**
          @author Nico Pauer
          @date February 8, 2023. UPDATED : February 15, 2023
          * Enable the firewall if it's disabled.
        **/
        if (!enabled)
        {
            enabled = true;
            System.out.println("FirewallBlockerP [ENABLED]")
        }
    }

    public static void disable()
    {
        /**
           @author Nico Pauer
           @date February 8, 2023. UPDATED : February 15, 2023
            * Disable the firewall if it's enabled.
        **/
        if (enable)
        {
            enabled = false;
          // Close the file by security
            f.close()
            fWriter.close();
            System.out.println("FirewallBlockerP [DISABLED]")
        } 
    }

    public static void blocking()
    {
      /**
        @author Nico Pauer
        @date February 8, 2023. UPDATED : February 15, 2023
        * Write blocked addresses to blocks file.
       **/
        for (String address : blocked)
        {
            System.out.println("IP address " + address + " has been blocked.");
            block(address);
        }
      // Close the file by security
        f.close()
        fWriter.close();
    }
}
