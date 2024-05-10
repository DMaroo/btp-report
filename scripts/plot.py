from matplotlib import pyplot as plt

## atomicAdd

### racefree

aa_rf_x = [0,1,2,3,4,5,6]
aa_rf = [3860,3900,3880,3800,3860,3930,4590]
aa_rf_ts = [8700,11600,20700,39000,97200,350000,1365000]

### racy

aa_rc_x = [0,1,2,3,4,5,6]
aa_rc = [3560,3540,3780,3830,4000,4080,4370]
aa_rc_ts = [9780,16300,28100,57600,144000,506000,1973000]

## Matrix

### racefree

mat_rf_x = [1,2,3,4,5]
mat_rf = [3610,3520,3960,4500,3970]
mat_rf_ts = [3860,4770,9200,46000,772700]

### racy

mat_rc_x = [1,2,3,4,5]
mat_rc = [3750,3840,4030,4050,4130]
mat_rc_ts = [4500,4900,10270,60000,1106000]


plt.rcParams['text.usetex'] = True

fig, ax = plt.subplots()
ax.plot(aa_rc_x, aa_rc_ts, marker='o', label='Racy reduction with ThreadSanitizer')
ax.plot(aa_rf_x, aa_rf_ts, marker='o', label='Racefree reduction with ThreadSanitizer')
ax.legend()
plt.xlabel(r"Kernel launch size parameter ($K$)")
plt.ylabel("Time taken by the kernel in microseconds")
plt.yscale('log')
plt.show()

fig, ax = plt.subplots()
ax.plot(mat_rc_x, mat_rc_ts, marker='o', label='Racy matrix multiplication with ThreadSanitizer')
ax.plot(mat_rf_x, mat_rf_ts, marker='o', label='Racefree matrix multiplication with ThreadSanitizer')
ax.legend()
plt.xlabel(r"Kernel launch size parameter ($K$)")
plt.ylabel("Time taken by the kernel in microseconds")
plt.yscale('log')
plt.show()


fig, ax = plt.subplots()
ax.plot(aa_rf_x, aa_rf_ts, marker='o', label='Racefree reduction with ThreadSanitizer')
ax.plot(aa_rf_x, aa_rf, marker='o', label='Racefree reduction')
ax.legend()
plt.xlabel(r"Kernel launch size parameter ($K$)")
plt.ylabel("Time taken by the kernel in microseconds")
plt.yscale('log')
plt.show()

fig, ax = plt.subplots()
ax.plot(aa_rc_x, aa_rc_ts, marker='o', label='Racy reduction with ThreadSanitizer')
ax.plot(aa_rc_x, aa_rc, marker='o', label='Racy reduction')
ax.legend()
plt.xlabel(r"Kernel launch size parameter ($K$)")
plt.ylabel("Time taken by the kernel in microseconds")
plt.yscale('log')
plt.show()

fig, ax = plt.subplots()
ax.plot(mat_rf_x, mat_rf_ts, marker='o', label='Racefree matrix multiplication with ThreadSanitizer')
ax.plot(mat_rf_x, mat_rf, marker='o', label='Racefree matrix multiplication')
ax.legend()
plt.xlabel(r"Kernel launch size parameter ($K$)")
plt.ylabel("Time taken by the kernel in microseconds")
plt.yscale('log')
plt.show()

fig, ax = plt.subplots()
ax.plot(mat_rc_x, mat_rc_ts, marker='o', label='Racy matrix multiplication with ThreadSanitizer')
ax.plot(mat_rc_x, mat_rc, marker='o', label='Racy matrix multiplication')
ax.legend()
plt.xlabel(r"Kernel launch size parameter ($K$)")
plt.ylabel("Time taken by the kernel in microseconds")
plt.yscale('log')
plt.show()
