TODO: be punchier about what's new, why it's important --> impacts
TODO: make sure we quantify errors in all the results we present

Introduction
------------

* explain outline
* Mountains are important in atmospheric flows at all scales: give some examples
* We model flow around mountains by solving the equations of motion using numerical schemes on meshes that represent the terrain and the air above it
* So, I have been looking at ways to improve meshes and numerical schemes
* What numerical errors are associated with orography: advection errors, horizontal pressure gradient errors
* there has been a desire to make grids more orthogonal to reduce these errors
* Introduce TF (BTF, and SLEVE) and cut cell meshes
* other meshes exist, too! (show slide)
* Show an example of pressure gradient errors with resting atmosphere animations (on BTF and ASAM cut cell meshes if possible)
* Show an example of advection errors with horizontal advection animations (on BTF and ASAM cut cell meshes if possible)
* So more orthogonal grids can reduce numerical errors
* BUT there are other difficulties: cut cell meshes suffer from the 'small cell problem' which limits the timestep we can take for explicit numerical schemes
* there are existing techniques to alleviate the small cell problem that involve modifying the mesh or the numerical schemes
* AND, we can perform other idealised tests that reveal errors that can appear on cut cell meshes

Today I will be focusing on idealised, 2D advection tests:

* I'll present a new type of mesh, the slanted cell mesh and talk about some of its advantages over TF and cut cell meshes
* I'll describe the advection scheme we are using, and how I'm currently improving it
* I will present a new advection test and evaluate results of the advection scheme on terrain following, cut cell and slanted cell meshes


Slanted cell meshes
-------------------

* An alternative way of alleviating the small cell problem
* Demonstrate how we construct a slanted cell mesh (I'd love to do this with props)
* We avoid creating very small cells when we move vertices down
* Thin cells are long in the direction of the flow


Multidimensional advection scheme
---------------------------------

We are using the finite volume method on arbitrary meshes.  This means we can use the same numerical scheme and compare results on different mesh types.

Explicit, Eulerian, multidimensional advection scheme

* we use the finite volume method, solving the flux form of the advection equation
* hence, we must approximate the value at the face using known values at surrounding cell centres (TODO: a little bit of maths might help to show why this is necessary)
* in the interior of domain, away from the boundaries, we fit a polynomial surface over a 12-point stencil (show slide with stencil and polynomial equation)
* in 2D, the polynomial is cubic in x, quadratic in y, giving us an equation with nine unknown coefficients (point to equation)
* hence, this problem is overspecified, and we use Singular Value Decomposition to provide a least squares fit (probably need to show some maths here about how we construct the matrix)
* show animated example from gnuplot of a polynomial surface, notice how the surface does not go exactly through every point
* we estimate the value at the face by reading off the value from the polynomial surface

Near the boundaries, we may not have sufficient data to fit the entire polynomial
* show slide with example of slanted cell mesh, highlighting the face and prevailing wind direction, and what stencil data we have
* I'm currently modifying the advection scheme to cope with such situations and identify which terms of polynomial to remove
* Returning to our matrix equation, the problem becomes the identification of linearly dependent columns (remind people what this means, and what column rank/full rank/rank deficiency mean on the whiteboard)
* We do this by constructing the matrix one column at a time, and checking if the matrix is still full rank.  We omit any terms that cause the matrix to become rank-deficient.

This aspect is work-in-progress, and I'll show some preliminary results in the next part of the talk.


Thermal advection test
----------------------
We'll compare the accuracy of the multidimensional advection scheme on our new slanted cell mesh against BTF and cut cell meshes using a newly formulated advection test.

Early we saw an advection test of a tracer blob in a horizontal wind field.  We have formulated a new advection test:
	- instead of a tracer blob, we advect an entire, stratified potential temperature field
	- we prescribe a wind field that is parallel to the terrain following surfaces

* This test is designed to mimic the advection of potential temperature in a complete atmospheric dynamical core
* It has an analytic solution, so we can calculate numerical errors
* Unlike the tracer blob horizontal advection test, this new test:
	- has advection at the lower boundary
	- has a wind field that has a vertical as well as horizontal component.  This presents a challenge to the advection scheme on more orthogonal meshes.

Present results with h0=1km, dz=250m on BTF, ASAM cut cell and slanted cell mesh, without adaptive polynomial fits.

TODO: unstable result on slanted cell mesh.  Now show that adaptive polynomial fit makes the solution stable.  TODO: animations of fixed/adaptive results on slanted cell mesh might be nice.

TODO: what is the max timestep on each mesh? (and so, have we addressed the small cell problem?)


Conclusions
-----------

(TODO: need to get all these results, but hopefully...)

We presented some new techniques for improving simulated flow around mountains:
1. a new slanted cell mesh 
   - simple to construct
   - allows longer timesteps than cut cell meshes
   - has smaller pressure gradient errors than TF meshes

2. an explicit, Eulerian, multidimensional advection scheme
   - mostly insensitive to grid distortions
   - mostly insensitive to misalignment of the flow with the grid
   - improvements to stability and boundary treatment are underway

TODO: can I make this punchier?  impacts?  inform choice of advection scheme for Dynamo at Met Office?


Next steps
----------

* Charney--Phillips for arbitrary meshes? (somewhat disconnected from the rest of this talk!)
