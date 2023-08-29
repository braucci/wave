import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def main():
    # Simulation parameters
    N = 256
    boxsize = 1.
    c = 1.
    t = 0
    tEnd = 2.
    plotRealTime = True

    # Mesh
    dx = boxsize / N
    dt = (np.sqrt(2)/2) * dx / c
    aX = 0
    aY = 1
    R = -1
    L = 1
    fac = dt**2 * c**2 / dx**2

    xlin = np.linspace(0.5*dx, boxsize-0.5*dx, N)
    Y, X = np.meshgrid(xlin, xlin)

    # Generate Initial Conditions & mask
    U = np.zeros((N,N))
    mask = np.zeros((N,N), dtype=bool)
    mask[0,:]  = True
    mask[-1,:] = True
    mask[:,0]  = True
    mask[:,-1] = True
    mask[int(N/4):int(N*9/32), :N-1]     = True
    mask[1:N-1, int(N*5/16):int(N*3/8)]  = False
    mask[1:N-1, int(N*5/8):int(N*11/16)] = False
    U[mask] = 0
    Uprev = 1.*U

    # Prep figure
    fig = plt.figure(figsize=(6,6), dpi=80)
    cmap = plt.cm.bwr
    cmap.set_bad('gray')
    outputCount = 1

    # Store frames for GIF
    image_list = []

    while t < tEnd:
        # Calculate laplacian 
        ULX = np.roll(U, L, axis=aX)
        URX = np.roll(U, R, axis=aX)
        ULY = np.roll(U, L, axis=aY)
        URY = np.roll(U, R, axis=aY)
        
        laplacian = (ULX + ULY - 4*U + URX + URY)

        # Update U
        Unew = 2*U - Uprev + fac * laplacian
        Uprev = 1.*U
        U = 1.*Unew

        # Apply boundary conditions
        U[mask] = 0
        U[0,:] = np.sin(20*np.pi*t) * np.sin(np.pi*xlin)**2

        # Update time
        t += dt

        print(t)

        if (plotRealTime) or (t >= tEnd):
            plt.cla()
            Uplot = 1.*U
            Uplot[mask] = np.nan
            plt.imshow(Uplot.T, cmap=cmap)
            plt.clim(-3, 3)
            ax = plt.gca()
            ax.invert_yaxis()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.set_aspect('equal')

            # Convert to RGB using colormap
            normed_data = (Uplot.T + 3) / 6  # Normalize to 0-1
            rgba_data = (cmap(normed_data) * 255).astype(np.uint8)  # Get RGBA data scaled to 0-255
            im = Image.fromarray(rgba_data, 'RGBA')  # Create PIL Image
            
            image_list.append(im)

            plt.pause(0.001)
            outputCount += 1

    # Save as GIF
    image_list[0].save('wave_simulation.gif',
                       save_all=True, append_images=image_list[1:], loop=0, duration=50)

    # Save as PNG (last frame)
    plt.savefig('finitedifference.png', dpi=240)
    plt.show()

    return 0

if __name__ == "__main__":
    main()
