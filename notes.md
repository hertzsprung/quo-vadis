Introduction
------------

* introduce title of talk

* We model flow around mountains by solving the equations of motion using numerical schemes on meshes that represent the terrain and the air above it
* So, I have been looking at ways to improve meshes and numerical schemes

* explain outline
  - I'll illustrate just a few effects that orography has on the weather
  - I'll discuss some existing types of mesh, and the types of numerical errors that arise when we model flow over orography
  - I'll present a new type of mesh, the "slanted cell" mesh, and talk about some of its advantages over existing mesh types
  - I'll describe an advection scheme that is suitable for any type of mesh, and how I'm currently improving it
  - I will present a new advection test and evaluate results of the advection scheme on several types of mesh, including the new "slanted cell" mesh

Effects of orography on the weather
-----------------------------------
* Mountains are important in altering atmospheric flows

Rain shadow
- Pictured: Agasthiyamalai hills, India

Thermally-driven circulation
- Pictured: Salt Lake Valley
Generates flows along valleys, and up and down slopes

Downslope windstorms
- High-amplitude gravity waves can create very strong flows
- Pictured: Boulder windstorms 1969, 130mph

Meshes & numerical error
------------------------

* first, let's consider meshes
* it is often true that distortions in a mesh lead to larger numerical errors
* hence, there has been a desire to make meshes more orthogonal
* introduce TF (BTF, and SLEVE) and cut cell meshes
* not all meshes are orthogonal, other meshes exist, too! (show slide)

* what numerical errors are associated with orography?
1. pressure gradient errors
   - we will demonstrate this with an idealised, 2D test
   - idealised wave-like mountain profile
   - stratified atmosphere initially at rest
   - distortions in the mesh cause errors calculating the pressure gradient
   - give rise to spurious circulations
* Show an example of pressure gradient errors with resting atmosphere animations (on BTF and cut cell meshes)

2. advection errors
   - define a tracer "blob" and advect it horizontally above another idealised mountain range
   - the true, analytic solution preserves its shape and intensity
* Show an example of advection errors with horizontal advection animations (on BTF and cut cell meshes)
  - these results use a centred finite volume advection scheme
  - notice a computational mode: grid-scale waves travelling in the opposite direction, typical of centred schemes

* So, these tests suggest that more orthogonal grids can reduce numerical errors
* BUT there are other difficulties: (show slide) cut cell meshes suffer from the 'small cell problem' which limits the timestep we can take for explicit numerical schemes
* there are existing techniques to alleviate the small cell problem that involve modifying the mesh or the numerical schemes
* later in the talk, I will show another difficulty with cut cell meshes

* (show section conclusion slide), conclude section #2



Slanted cell meshes
-------------------

* I wanted to create a mesh that reduces pressure gradient errors and advection errors
* AND avoid the small cell problem associated with cut cell meshes
* show example of a slanted cell mesh over another idealised mountain
* constructed by moving vertices up/down, snapping them to the terrain
* (show with wind field) -- unlike cut cell meshes, the thin cells are still long in the direction of the flow

* (show section conclusion slide), conclude section #3


Multidimensional advection scheme
---------------------------------

I am using the finite volume method on arbitrary meshes.  This means we can use the same numerical scheme and compare results on different mesh types.

Explicit, Eulerian, multidimensional advection scheme

* we solve the flux form of the advection equation
* hence, we must approximate the value at the face using known values at surrounding cell centres

* in the interior of domain, away from the boundaries, we fit a polynomial surface over a 12-point stencil (show slide with stencil and polynomial equation)
* in 2D, the polynomial is cubic in x, quadratic in y, giving us an equation with nine unknown coefficients (point to equation)
* (next slide) hence, this problem is overspecified and we must use a least squares approach to fit the polynomial surface

* show animated example from gnuplot of a polynomial surface
  - green crosses are our known values of some tracer, T
  - notice how the surface does not go exactly through every point
* we estimate the value at the face by reading off the value from the polynomial surface
  - this is the yellow lollipop in the animation

* Near the boundaries, we may not have sufficient data to fit the entire polynomial
  - (show inlet boundary slide) we have 9 knowns and 9 unknowns, ASK AUDIENCE: do you think, then, that we can fit this polynomial?
  - (next slide) answer: NO, we don't have sufficient information to fit the x^3 term
  - (next slide) as well as the inlet boundary, there may not be enough data near the lower boundary
    * in this example, heavy purple lines show faces where we cannot fit all 9 terms

* I'm currently modifying the advection scheme to cope with such situations and identify which terms of polynomial to remove

* (show section conclusion slide), conclude section #4
  - this "adaptive polynomial fit" is work-in-progress, and I'll show some preliminary results later in the talk


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

**Results**

* First, let's look at results without using the new "adaptive polynomial fit"
  - these are plots of the difference between numerical and analytic solutions
  - colour scale ranges from -1 to +1

  - small errors on BTF mesh
  - much larger errors on slanted cell mesh
  - (next slide) solution is unstable on the cut cell mesh -- there's that computational mode again: grid scale oscillations travelling against the wind

* So, does the new "adaptive polynomial fit" improve stability and accuracy?
  - (next slide) YES: solution is now stable on the cut cell mesh
  - errors are much smaller on the slanted cell mesh (compared with bottom panel)

* (show summary table) Summarize: 
  - this test present little challenge to the BTF meshes
  - but it does challenge the more orthogonal meshes
  - we need to use the adaptive polynomial fit to achieve stability and improve accuracy

* These results used Courant numbers very close to 1 (the maximum permitted)
  - (show timestep slide) slanted cell meshes allow timesteps comparable to BTF, avoids the small cell problem on the cut cell mesh

* So why not use the BTF grid?
  - we need to remember those pressure gradient errors
  - (show slide) spurious circulations on the slanted cell mesh are even smaller than the cut cell mesh!


Numerical representation of orography in dynamical cores
--------------------------------------------------------

We've looked at:
1. some effects that orography has on the weather
2. some existing types of mesh, and looked at advection errors and pressure gradient errors
3. we presented a new "slanted cell mesh" that seeks to reduce these errors
4. and an "adaptive polynomial fit" to improve stability and accuracy of our advection scheme
5. we evaluated our advection scheme and our slanted cell mesh in a new advection test


Conclusions
-----------

We've shown that:
1. the new slanted cell mesh
   - allows much longer timesteps than cut cell meshes
   - has smaller pressure gradient errors than BTF or cut cell meshes

2. the new "adaptive polynomial fit" provides better stability and accuracy for the multidimensional advection scheme


Next steps
----------

* we're taking a more rigorous approach to make advection scheme stable and more accurate, using von Neumann stability analysis
* next, I will move towards a full dynamical core suitable for arbitrary meshes
* I want to formulate a new staggering of variables that is free from computational modes
* and extend the multidimensional advection scheme for use on these meshes
