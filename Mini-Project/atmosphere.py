# atmosphere.py

import numpy as np
from scipy.constants import G, R as Rg
from scipy.interpolate import interp1d
from scipy.constants import k 

class Atmosphere:
    def __init__(self, params):
        self.params = params
        self._load_cross_section()

    def _load_cross_section(self):
        # Load CO2 cross section file with colums nu, sigma, k 
        data = np.loadtxt(
            self.params["cross_section_file"],
            skiprows=15
        )
        
        nu = data[:, 0]            # [cm^-1]
        sigma_cm2 = data[:, 1]     # [cm^2/molecule]
        k = data[:, 2]             # [m^-1] 

        # Convert wavenumber to wavelength in microns
        lam_um = 1e4 / nu             # [µm]

        # Convert cross section to m^2 / molecule
        sigma_m2 = sigma_cm2 * 1e-4

        self.sigma_interp = interp1d(
            lam_um,
            sigma_m2,
            bounds_error=False,
            fill_value=0.0
        )

    def scale_height(self):
        g = G * self.params["Mpl"] / self.params["Rpl"]**2
        H = k * self.params["Tatm"] / (self.params["mgas"] * g)
        return H

    def number_density(self, R):
        # barometric formula 
        h = R - self.params["Rpl"]
        H = self.scale_height()
        return self.params["rho_surf"] * np.exp(-h / H)

    def column_density(self, R):
        # approximation of column density 
        N = self.number_density(R)
        H = self.scale_height()
        return N * np.sqrt(2 * np.pi * R * H)

    def optical_depth(self, lam_um, R):
        sigma = self.sigma_interp(lam_um)
        Nt = self.column_density(R)
        tau = Nt * sigma
        T = np.exp(-tau)
        return tau, T


def opticaldepth(lam_um, R):
    # Wrapper function so the module can be used as:     
    # atmosphere.opticaldepth(lambda, R)
    from params import params
    atm = Atmosphere(params)
    return atm.optical_depth(lam_um, R)

