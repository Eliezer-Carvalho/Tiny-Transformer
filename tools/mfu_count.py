import humanize

#MFU #Model FLOPs Utilization
#Atenção à variável seconds, é melhor correr durante vários steps e calcular uma média de segundos
#FLOPs_Teóricos é uma variável do fabricante 
def mfu (FLOPs, seconds, FLOPs_Teóricos):
    
    #FLOPS é o número de de FLOPs por segundo
    FLOPS = FLOPs / seconds #Achieved Flops #Throughput real

    MFU = FLOPS / FLOPs_Teóricos #Throughput teórico #Percentagem


    print (humanize.scientific(FLOPS))
    print (f"{round(MFU * 100, 3)}%")


mfu (25e10, 7.5, 65.13e12)


#MFLOPs	10e6
#GFLOPs	10e9
#TFLOPs	10e12
#PFLOPs	10e15