# Imports
import pyglet
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.gl import GL_TRIANGLES
from pyglet.math import Mat4, Vec3

# Window
window = pyglet.window.Window(width=1280, height=720, caption='Shaders')

# Vertex source
vertex_source = """
#version 330
layout(location = 0) in vec2 vertices;
layout(location = 1) in vec4 colors;

out vec4 newColor;

void main() {
    gl_Position = vec4(vertices, 0.0f, 1.0f);
    newColor = colors;
}
"""

# Fragment source
fragment_source = """
#version 330
in vec4 newColor;

out vec4 outColor;

void main() {
    outColor = newColor;
}
"""

# Compile the vertex and fragment sources toa  shader program
vert_shader = Shader(vertex_source, 'vertex')
frag_shader = Shader(fragment_source, 'fragment')
program = ShaderProgram(vert_shader, frag_shader)

# Create the view and (orthogonal|orthographic) projection matrices
view_mat = Mat4.from_translation(Vec3(x=0, y=0, z=-1))
proj_mat = Mat4.orthogonal_projection(left=0, right=1280, bottom=0, top=720, z_near=0.1, z_far=100)


# Combine the view and projection matrices into one matrix

# Upload the combines vp matrix to the vertex shader vp uniform

# Create the model matrix and upload it to the model uniformd

# Batch
batch = pyglet.graphics.Batch()

# Add a vertex list to the shader program
# program.vertex_list(3, GL_TRIANGLES,
#                     batch=batch,
#                     vertices=('f', (-0.5, -0.5, 0.5, -0.5, 0.0, 0.5)),
#                     colors=('Bn', (255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255)),
#                     )
#

program.vertex_list_indexed(4, GL_TRIANGLES,
                            batch=batch,
                            indices=(0, 1, 2, 2, 3, 0),
                            vertices=('f', (-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5)),
                            colors=('Bn', (255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255, 255, 255, 255, 255)))


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
