package Default;

import java.io.*;

public class BlockUpdater
{
  /**
     @author Nico Pauer
     @date February 8, 2023. UPDATED : February 16, 2023
    * Manage and update info about blocked IP addresses in a binary file providing services
      to FireblockerP class.
 **/
  // Properties
    private File f;
    private FileWriter fWriter;
 // Constructors

    public BlockUpdater()
    {
        f = new File("blocks.IP");
        fWriter = new FileWriter(f); // Use this for Writing in the file
    }

    public BlockUpdater(File fi)
    {
        f = fi;
    }
  // Methods
    public static bool isBlocked(String IP)
    {
       /**
        @author Nico Pauer
        @date February 8, 2023. UPDATED : February 14, 2023
        * Search for the IP address in the file that contains the lines with the blocked IP addresses.
       **/
        boolean wanted_result = false
        BufferedReader buff = new BufferedReader(f);
        while (buff.readLine() != null)
        {
         // I want if the IP is blocked while the file continue or found that the IP is in the file
        // If the IP isn't in the file then this isn't blocked
            wanted_result = (buff.readLine() == IP)
        }
        return wanted_result;
    }

    public static void block(String IP)
    {
      /**
        @author Nico Pauer
        @date February 8, 2023. UPDATED : February 15, 2023
        * Add IP to the file if this isn't in blocks file.
       **/
        PrintWriter buffW = new PrintWriter(fWriter);
        if (!isBlocked(IP))
        {
            buffW.println(IP);
            System.out.println("[" + IP + "] is blocked now.");
        }
    } 

    public static void unblock(String IP)
    {
      /**
        @author Nico Pauer
        @date February 8, 2023. UPDATED : February 16, 2023
        * Remove IP from the file if this is in blocks file.
      **/
        BufferedReader initialFile = new BufferedReader(f);
        PrintWriter endFile = new PrintWriter(fWriter);
      // Copy all the IP addresses less the IP address to unblock in the file
        while (initialFile.readLine() != null)
        {
            if (initialFile.readLine() == IP)
            {
              // If the line is the address to unblock then delete it from the file
                endFile.println("");
            }
        }
    }
}
