import math

# the angle with respect to the beam axis of the particle
def Theta(event, i):
    # if calculating only for one particle
    if i != 2:
        p_z_sum = event.particles[i].pz
        p = event.particles[i].E
    # if calculating for a pair -> e.g. xi with pseudorapidity (using constant indexes)
    else:
        p_z_sum = event.particles[3].pz + event.particles[4].pz

        # WRITE ANDRE THAT IT WORKS ONLY WITH ENERGY AND NOT MOMENTUM
        p = event.particles[2].E

    cos_theta = p_z_sum/p
    
    return math.acos(cos_theta)

# pseudorapidity
def Eta(event, i):
    t = Theta(event, i)
    
    return -math.log(math.tan(t/2))

def TransverseMomentum(event, i):
    return (event.particles[i].px ** 2 + event.particles[i].py ** 2) ** 0.5

# proton relative energy loss
def XiProton(event, i, energy_before):
    return (energy_before - event.particles[i].E)/energy_before

# pair energy loss with pseudorapidity - always calculated for the pair as whole
# -> constant index 2
# returns values for A side and C side
def XiEta(event, sqrt_s):
    eta = Eta(event, 2)

    xi_A = event.particles[2].M/sqrt_s * math.exp(-eta)
    xi_C = event.particles[2].M/sqrt_s * math.exp(eta)

    return xi_A, xi_C

# pair energy loss with rapidty - always calculated for the pair as whole
# -> constant index 2
# returns values for A side and C side
def XiY(event, sqrt_s):
    E = event.particles[2].E # photon-pair energy
    pz = event.particles[2].pz # photon-pair P_z

    y_A = (1/2)*math.log((E - pz)/(E + pz))
    y_C = (1/2)*math.log((E + pz)/(E - pz))

    xi_A = event.particles[2].M/sqrt_s * math.exp(y_A)
    xi_C = event.particles[2].M/sqrt_s * math.exp(y_C)

    return xi_A, xi_C

def Acoplanarity(event):
    p1x = event.particles[3].px
    p1y = event.particles[3].py

    p2x = event.particles[4].px
    p2y = event.particles[4].py

    p1 = (p1x**2 + p1y**2)**0.5
    p2 = (p2x**2 + p2y**2)**0.5

    angle = math.acos((p1x*p2x + p1y*p2y)/(p1*p2))
    
    a = 1 - abs(angle/math.pi)

    return a