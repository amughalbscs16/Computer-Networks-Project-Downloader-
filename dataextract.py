from tcpfunctions import *

#Extract Data from the command line arguments
def getCommandLineArguments(arguments):
    """
    Function: self written parser for arguments
    param arguments: input command line arguments"
    return: cleaned arguments
    """
    resume=False
    connections=0
    tInterval=0;
    cType=""
    fileLocWeb = "";
    fileWebName = "";
    fileLocPc = "";
    filePcName = "";
    serverHost="";
    serverDownDirectory="";
    for i in range(0,len(arguments)):
        #Parse each of the flag and store the data corresponding to that.
        if arguments[i]=="-r":
            resume=True;

        if arguments[i]=="-n":
            connections=int(arguments[i+1])

        if arguments[i]=="-i":
            tInterval=float(arguments[i+1])

        if arguments[i]=="-c":
            cType = arguments[i+1]

        if arguments[i]=="-f":
            fileLocWeb = arguments[i+1];
            fileWebName = fileLocWeb.split('/')[-1]
            for i in range(3,len(fileLocWeb.split("/"))):
                serverDownDirectory+="/"+fileLocWeb.split("/")[i];
            
        if arguments[i]=="-o":
            fileLocPc = arguments[i+1]
            filePcName = fileWebName
            print(fileLocPc)
            if fileLocPc == ".":
                fileLocPc = sys.path[0]

            fileLocPc+="/"+filePcName #"\\" for windows "/" for ubuntu;

    serverHost=fileLocWeb.split("://")[1].split("/")[0];
    return (serverHost,resume,connections,tInterval,cType,fileLocWeb,fileWebName,serverDownDirectory,fileLocPc)

def getChunksList(dataSize,recvSize):
    """
    Function: Divides the file into chunks
    param dataSize: The size of file total - integer
    param recvSize: The size of chunk to recieve - integer
    return: A List of each chunk's download information - list
    """
    #Each chunk contains a list of [Downloaded,start,end,InUse]
    chunkList=[[False,j*recvSize,(j+1)*recvSize-1,False] for j in range((int(dataSize/recvSize))+1)]
    chunkList[-1][2] = dataSize;
    return chunkList;
