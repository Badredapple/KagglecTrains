# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 14:05:33 2017

@author: DKjack
"""
##http://nbviewer.jupyter.org/github/unpingco/Python-for-Signal-Processing
from scipy import signal
import numpy as np
import math
import matplotlib as plt

# some useful functions 
def dftmatrix(Nfft=32,N=None):
    'construct DFT matrix'
    k= np.arange(Nfft)
    if N is None: N = Nfft
    n = arange(N)
    U = matrix(exp(1j* 2*pi/Nfft *k*n[:,None])) # use numpy broadcasting to create matrix
    return U/sqrt(Nfft)


def db20(W,Nfft=None):
    'Given DFT, return power level in dB'
    if Nfft is None: # assume W is DFT 
        return 20*log10(abs(W))
    else: # assume time-domain passed, so need DFT
        return 20*log10(abs( fft.fft(W,Nfft)/sqrt(Nfft) ) )

fs = 64 # sampling frequency
t = arange(0,2,1/fs)
f = 10  # one signal
deltaf = 2.3 # second nearby frequency

Nf = 512
fig,ax = subplots(2,1,sharex=True,sharey=True)
fig.set_size_inches((9,4))

x=10*cos(2*pi*f*t) + 10*cos(2*pi*(f+deltaf)*t) # equal amplitudes
X = fft.fft(x,Nf)/sqrt(Nf)
ax[0].plot(linspace(0,fs,len(X)),abs(X),'-o',ms=3.)
ax[0].set_ylabel(r'$|X(k)|$',fontsize=18)
ax[0].set_xlim(xmax = fs/2)
ax[0].grid()
ax[0].text(0.5,0.5,'Same amplitudes',
            transform=ax[0].transAxes,
            backgroundcolor='Lightyellow',
            fontsize=16)

x=cos(2*pi*f*t) + 10*cos(2*pi*(f+deltaf)*t) # one has 10x the amplitude
X = fft.fft(x,Nf)/sqrt(Nf)
ax[1].plot(linspace(0,fs,len(X)),abs(X),'-o',ms=3.)
ax[1].set_ylabel(r'$|X(k)|$',fontsize=18)
ax[1].set_xlabel('Frequency (Hz)',fontsize=18)
ax[1].set_xlim(xmax = fs/2)
ax[1].grid()
ax[1].text(0.5,0.5,'Different amplitudes',
                transform=ax[1].transAxes,
                backgroundcolor='lightyellow',
                fontsize=16)
ax[1].annotate('Smaller signal',
            fontsize=12,xy=(f,abs(X)[int(f/fs*Nf)]),
            xytext=(2,15),
            arrowprops={'facecolor':'m','alpha':.3});

# fig.savefig('figure_00@.png', bbox_inches='tight', dpi=300)
