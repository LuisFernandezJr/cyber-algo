import os

# set folder directory
readPCAPDirectory = "/Users/jonathan/Downloads/downloaded_pcaps/Malicious/pcaps"
readCSVDirectory = "/Users/jonathan/Downloads/downloaded_pcaps/Malicious/initialcsvs"
writeCSVDirectory = "/Users/jonathan/Downloads/downloaded_pcaps/Malicious/updatedcsvs"

# set the maliciousness
isMalicious = 1

headers = "IP Source,IP Destination,Source Port,Destination Port,TCP Flag Nonce,TCP Flag Congestion Window Reduced,TCP Flag ECN-Echo,TCP Flag Urgent,TCP Flag Acknowledgement,TCP Flag Push,TCP Flag Reset,TCP Flag Syn,TCP Flag Fin,Malicious\n"

# traverse all files in the Directory
# convert from pcap to csv
# write the headers
# write the line with new data appended to it

# pcap -> initial csv
# comment this out if pcaps are already in csv format
# that will make it faster
for root, firs, files in os.walk(readPCAPDirectory):
    for file in files:
        if file.endswith(".pcap"):
            tsharkFunction = "tshark -2 -r " + os.path.join(root, file) + " -R \"tcp\" -E separator=, -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.flags.ns -e tcp.flags.cwr -e tcp.flags.ecn -e tcp.flags.urg -e tcp.flags.ack -e tcp.flags.push -e tcp.flags.reset -e tcp.flags.syn -e tcp.flags.fin > " + os.path.join(readCSVDirectory, file) + ".csv"
            os.system(tsharkFunction)

# initial csv -> updated csv
for root, dirs, files in os.walk(readCSVDirectory):
    for file in files:
        if file.endswith(".csv"):
            readFile = open(os.path.join(root, file), "r")
            writeFile = open(writeCSVDirectory + "/updated_" + file, "w")

            # comment out the following line to not have the column headers write out
            writeFile.write(headers)

            for line in readFile:
                updatedLine = line.replace("\n", ",") + str(isMalicious) + "\n"
                writeFile.write(updatedLine)

            readFile.close()
            writeFile.close()

        
