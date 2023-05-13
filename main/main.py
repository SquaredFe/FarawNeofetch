# Neofetch for Faraw VER 1 REV 2
import os, platform, subprocess, re
total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
 
def get_processor_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    return ""

print("              &#BGGGPPPPPPPGGBB&          user@faraw")
print("          &&  BGGBB##&&&&&##BBG#  ##&     ----------")
print("       &BGPB                      BPPG#&  OS: Faraw")
print("     &BPPB&         &&&&&           #GPG  Host: FR0381")
print("    BPPB&      &BGGPPPGGG#  #B#&          Kernel: python3")
print("  &GPG&     &BPPGB#&&&      #GGPGB&       Packages: 3")
print(" &GPB     &GPPB&               &BPPB&     Shell: FarawMain")
print(" GPG     &GPB      &&#BB##&      &GPG#    DE: None")
print("&GG&      &&     #GPPGGGGGPPB&     #PP#   Theme: Default")
print("        BG&     BPP#&     &BPP#     BPP&  Terminal: gnome-terminal")
print("BG#    &PP#     BB&         &#&      GPB  CPU:" + get_processor_name())
print("PPB    &PPB                   ##      &   RAM: " + str(round((used_memory/total_memory) * 100, 2)) + "% / 100%")
print("GPG     BPG                  #PP&    &B#   ")
print("&PP#    &GPG&               &GPB     GPG")
print(" BPP&    &BPP#             #GPB     #PP#")
print("  BPP#     #GPPB#     &&#BGPG#     #PP# ")
print("    &GPG            &&&&       &#GPG&   ")
print("      && &B#&                #GPPG#        __________ ")
print("         &GGPGGB##&&&&&##B#  #B#&         |FABCDEFGHI|")
print("            &#BGGPPPPPPPGGB               |0123456789|")
print("                                           ----------")
print("Presiona ENTER para cerrar...")
input()