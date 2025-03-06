import numpy as np

done = False
n_discs = 1070379110497-1#int(int(1E12)+1)

while not done:
    num = n_discs * (n_discs-1)
    exceed_half = False

    # nb = int(np.floor(n_discs*0.70707)) # start assuming n_b is half of num
    nb = int(np.ceil(  0.5 * ( 1 + np.sqrt(float(1 + 2 *(n_discs-1)*n_discs)) )  ))-1
    # nb =  np.sqrt(2 *(n_discs**2-n_discs) )



    while not exceed_half:

        denom = (nb * (nb-1))*2
        print(f'n_discs={n_discs}, nb={nb}, num/denom={num/denom}')

        if num > denom:
            nb += 1
        else:
            if num == denom:
                print(f'Done. Solution: n_discs={n_discs}, nb={nb} ')
                done = True
                break
            else:
                print(f'n_discs={n_discs} does not work')
                exceed_half = True

    n_discs += 1
















