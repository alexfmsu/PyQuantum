# --------------------
from math import sqrt
from numpy import arange

KHz = 10 ** 3  # 1 KГц
MHz = 10 ** 6  # 1 МГц
GHz = 10 ** 9  # 1 ГГц

ms = 1e-3  # 1 мс
mks = 1e-6  # 1 мкс
ns = 1e-9  # 1 мкс
# --------------------
# BEGIN----------------------------------------- CAVITY -------------------------------------------
capacity = 2

wc = 21.506 * GHz
wa = 21.506 * GHz

# wc = 6.34 * GHz
# wa = 6.34 * GHz

g_list = arange(0.01, 0.02, 0.01) * 1e-2
# g = 190 * MHz
# g = 1e-2 * 21.506 * GHz
# g = 1.0 * 1e-1 * 21.506 * GHz
# g = 1.0
# g = 1e-2 * 21.506 * GHz

n_atoms = 2

n_levels = 2
# END------------------------------------------- CAVITY -------------------------------------------

# -------------------------------------------------------------------------------------------------
l_list = arange(1.1, 1.2, 0.1)
# l = g * 1	e1

sink_threshold = 0.001
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
precision = 5
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# T = 1
# T = 100
# T = 1 * mks
# T = 0.25 * mks
# T = 0.5 * mks
# T = 1 * mks
# T = 5 * mks
# T = 0.5 * mks

# dt = T / nt
# dt = T / 500
# dt = T / 1000
# dt = (0.01/l)
# dt = (0.1/l)

# nt = 100
# nt = 1000
# nt = int(T*nt)
# nt = int(T/mks*nt)
# nt = int(T/dt)

# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
state_type = 't_0'
# state_type = 's_2'

# init_state = [0, [1, 1, 1, 1, 1]]
# init_state2 = [0, [1, 1]]
# init_state = [2, [0, 1, 0]]
# certain_state = [1, [0, 1]]
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
path = "PyQuantum/TCL/out/" + str(capacity) + "_" + str(n_atoms) + "/"

H_html = path + "H.html"
H_csv = path + "H.csv"
U_csv = path + "U.csv"
ro_0_csv = path + "ro_0.csv"
U_csv = path + "U.csv"
x_csv = path + "x.csv"
y_csv = path + "t.csv"
z_csv = path + "z.csv"
z_all_csv = path + "z_all.csv"
fid_csv = path + "fid.csv"
fid_small_csv = path + "fid_small.csv"
# -------------------------------------------------------------------------------------------------