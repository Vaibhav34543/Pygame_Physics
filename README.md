# Creating a physics engine in python-pygame
Just experimenting around with the pygame module from python and trying to build in some basic physics implementations.

## Gravitational Force implementation
The gravitation force was quite easy to do all i had to do was just to tweak some values of the masses of particles and change the value of G (Gravitational Constant) a little bit to get a nice elliptical orbit. Here's an image of how the path of a particle with some initial velocity != 0 is

<div display="flex">
<img src="https://github.com/Vaibhav34543/Pygame_Physics/blob/main/Gravitation_Force/Illustration2.png?raw=true" width=30%>
<img src="https://github.com/Vaibhav34543/Pygame_Physics/blob/main/Gravitation_Force/Illustration1.png?raw=true" width=30%>
</div>

The `gravitation(self, object1, object2)` from the `Forces` class does all the work behind here, using vectors it gives acceleration to the bodies in x, y directions and thus by tweaking the values we get a cool looking 2 planet, planetary motion 
