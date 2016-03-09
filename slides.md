Introduction
------------

DONE 1+ slide of some atmospheric flows in which mountains are important (one smallscale, one mid scale, one large scale?)
DONE BTF mesh
DONE SLEVE mesh
DONE ASAM cut cell mesh
DONE "and others" mesh
* Pressure gradient errors on BTF
* Pressure gradient errors on ASAM cut cell
DONE Horizontal advection errors on BTF
DONE Horizontal advection errors on ASAM cut cell
DONE ASAM cut cell mesh again, highlighting small cells

Slanted cell meshes
-------------------

* Example of a slanted cell mesh (from the h0=1km, dz=250m test?)

Multidimensional advection scheme
---------------------------------

DONE slide with (continuous) flux form advection equation, and spatial discretisation leaving phi\_F unspecified
DONE slide with 12-point stencil (with some TF style cells), and polynomial equation
DONE slide showing how we use the mesh geometry to construct a matrix equation (put the polynomial equation at the top)
* rotating animation of polynomial surface from gnuplot (pausing for a while after a rotation)

DONE spacebar-driven animation of column-by-column rank-deficient matrix construction

Thermal advection test
----------------------

* BTF error field
* ASAM cut cell grid error field
* slanted mesh, fixed polynomial error field
* slanted mesh, adaptive polynomial error field
* bar graph of max timesteps (fixed Courant number)

Conclusions and future work
---------------------------

* one slide
