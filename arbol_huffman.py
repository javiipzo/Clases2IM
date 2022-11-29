import os
import time
class Node:
    prob=0.0
    symbol=""
    encoding=""
    visited=False
    parent=-1

class HuffmanTree:
    Tree=None
    Root=None
    Nodes=[]
    probs={}
    dictEncoder={}

    def __init__(self,symbols):
        self.initNodes(symbols)
        self.buildTree()
        self.buildDict()

    def initNodes(self,probs):
        for symbol in probs:
            node=Node()
            node.symbol=symbol
            node.prob=probs[symbol]
            node.visited=False
            self.Nodes.append(node)
            self.probs[symbol]=probs[symbol]

    def getNodeWithMinProb(self):
        minProb=1.0
        indexMin=-1
        for index in range(0,len(self.Nodes)):
            if self.Nodes[index].prob<minProb and not self.Nodes[index].visited:
                minProb=self.Nodes[index].prob
                indexMin=index
        if indexMin!=-1:
            self.Nodes[indexMin].visited==True
        return indexMin



    def buildTree(self):
        IndexMin=self.getNodeWithMinProb()
        IndexMin2=self.getNodeWithMinProb()
        while IndexMin!=-1 and IndexMin2!=-1:
            node=Node()
            node.symbol="."
            node.encoding=""
            prob1=self.Nodes[IndexMin].prob
            prob2=self.Nodes[IndexMin2].prob
            node.prob=prob1+prob2
            node.visited=False
            node.parent=-1
            self.Nodes.append(node)
            self.Nodes[IndexMin].parent=len(self.Nodes)-1
            self.Nodes[IndexMin2].parent=len(self.Nodes)-1
            if prob1>=prob2:
                self.Nodes[IndexMin].encoding="0"
                self.Nodes[IndexMin2].encoding="1"
            else:
                self.Nodes[IndexMin].encoding="1"
                self.Nodes[IndexMin2].encoding="0"

            IndexMin=self.getNodeWithMinProb()
            IndexMin2=self.getNodeWithMinProb()



    def showSymbolEncoding(self,symbol):
        found =False
        index=0
        encoding=""
        for i in range(0,len(self.Nodes)):
            if self.Nodes[i].symbol==symbol:
                found=True
                index=i
                break
            
        if found:
            while index!=-1:
                encoding="%s%s" % (self.Nodes[index].encoding,encoding)
                index=self.Nodes[index].parent
        else:
            encoding="Simbolo desconocido"
            
        return encoding

    def buildDict(self):
        for symbol in self.probs:
            encoding=self.showSymbolEncoding(symbol)
            self.dictEncoder[symbol] = encoding

    def encode(self,plain):
        encoded=""
        for symbol in plain:
            encoded="%s%s" % (encoded,self.dictEncoder[symbol])
        return encoded
    
    def decode(self,encoded):
        index=0
        decoded=""
        while index<len(encoded):
            found=False
            aux=encoded[index:]

            for symbol in self.probs:
                if aux.startswith(self.dictEncoder[symbol]):
                    decoded="%s%s" % (decoded,symbol)
                    index=index+len(self.dictEncoder[symbol])
                    break
        return decoded

if __name__=="__main__":
    mensaje=input("Ingrese algo: ")
    simbolos=''
    probs=[]
    msn=mensaje
    d=0

    for i in msn:   
        #for i in msn:
        simbolos+=i
        probs.append(float(float(msn.count(i))/float(len(mensaje))))
        msn=msn.replace(i,'')
        d+=1
    print (probs)
    symbols=dict(zip(simbolos,probs))

    print(symbols)

    huffman=HuffmanTree(symbols)

    #for symbol in symbols:
        #print("Simbolo: %s, codificacion: %s" % (symbol,huffman.showSymbolEncoding(symbol)))