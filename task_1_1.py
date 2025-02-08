import numpy as np
from vis import *

class task_1_1:
    def __init__(self, fs=1000):
        """
        Initialize the class with a specific sampling rate.

        Args:
            fs (int): Sampling rate in Hz. Defaults to 1000Hz.
        """
        self.fs = fs
    
    # TODO: Implement this function
    def generate_signal_1(self):
        """
        Generate the first signal: a pure tone with a specified frequency and phase offset.

        Returns:
            numpy.array: Array of timestamps in seconds. Data type must be float.
            numpy.array: Array of generated signal values. Data type must be float.

        Note:
            - The returned signal array must strictly be of type float.

        Example:
            >>> gen = task_1_1(1000)
            >>> t, s_t = gen.generate_signal_1()
            >>> np.round(t[10], 5), np.round(s_t[10], 5)
            (-0.99, 0.6046)
        """  
        t = None
        s_t = None
        
        # >>>>>>>>>>>>>>> YOUR CODE HERE <<<<<<<<<<<<<<<
        #
        # >>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<
        t = np.linspace(-1, 1, 2*self.fs, endpoint=False)
        s_t = np.sin(4*np.pi*t + np.pi/6)
        
        return t, s_t

    # TODO: Implement this function
    def generate_signal_2(self):
        """
        Generate the second signal: a combination of rectangle and triangle waves.

        Returns:
            numpy.array: Array of timestamps in seconds. Data type must be float.
            numpy.array: Array of generated signal values. Data type must be float.

        Note:
            - The returned signal array must strictly be of type float.

        Example:
            >>> gen = task_1_1(1000)
            >>> t, s_t = gen.generate_signal_2()
            >>> np.round(t[10], 5), np.round(s_t[10], 5)
            (-0.99, 0.0)
        """
        
        t = np.linspace(-1, 1, 2*self.fs, endpoint=False)
        rect_wave = np.ones(t.shape)
        tri_wave = 1 - 5 * np.abs(t-0.5)
        
        rect_wave = np.where((t >= -0.7) & (t < -0.3), rect_wave, 0)
        tri_wave = np.where((t > 0.3) & (t <= 0.7), tri_wave, 0)
        
        s_t = rect_wave + tri_wave
        
        return t, s_t
        
    # TODO: Implement this function
    def generate_signal_3(self):
        """
        
        Generate the third signal: a complex signal based on real and imaginary parts.

        Returns:
            numpy.array: Array of timestamps in seconds. Data type must be float.
            numpy.array: Array of generated complex signal values. Data type must be np.complex64.

        Note:
            - The returned signal array must strictly be of type np.complex64.
            
        Example:
            >>> gen = task_1_1(1000)
            >>> t, s_t = gen.generate_signal_3()
            >>> np.round(t[10], 5), np.round(s_t[10], 5)
            (-0.99, (0.99211+0.12533j))
        """
        t = None
        s_t = None
        
        # >>>>>>>>>>>>>>> YOUR CODE HERE <<<<<<<<<<<<<<<
        #
        # >>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<
        t = np.linspace(-1, 1, 2*self.fs, endpoint=False)
        s_t = np.cos(4 * np.pi * t) + 1j * np.sin(4 * np.pi * t)
        return t, s_t
    
    def visualize(self):
        # Generate the first signal
        t, s_t = self.generate_signal_1()
        plot1D_single(t, s_t, '1-1', 'Time (s)', 'Amplitude')
        
        # Generate the second signal
        t, s_t = self.generate_signal_2()
        plot1D_single(t, s_t, '1-2', 'Time (s)', 'Amplitude')
        
        # Generate the third signal
        t, s_t = self.generate_signal_3()
        plot1D_multiple(t, [np.real(s_t), np.imag(s_t)], ['Real', 'Imaginary'], '1-3', 'Time (s)', 'Amplitude')
    