Introduction
------------

* 1+ slide of some atmospheric flows in which mountains are important (one smallscale, one mid scale, one large scale?)
* BTF mesh
* SLEVE mesh
* ASAM cut cell mesh
* Pressure gradient errors on BTF
* Pressure gradient errors on ASAM cut cell
* Horizontal advection errors on BTF
* Horizontal advection errors on ASAM cut cell
* ASAM cut cell mesh again, highlighting small cells

Slanted cell meshes
-------------------

* Example of a slanted cell mesh (from the h0=1km, dz=250m test?)

Multidimensional advection scheme
---------------------------------

* slide with (continuous) flux form advection equation, and spatial discretisation leaving phi\_F unspecified
* slide with 12-point stencil (with some TF style cells), and polynomial equation
* slide showing how we use the mesh geometry to construct a matrix equation (put the polynomial equation at the top)
* rotating animation of polynomial surface from gnuplot (pausing for a while after a rotation)

* slanted cell mesh with stencil for face near the boundary overlayed
* spacebar-driven animation of column-by-column full-rank matrix construction

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
