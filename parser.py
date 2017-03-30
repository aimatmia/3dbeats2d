from display import *
from matrix import *
from draw import *


ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'circle', 'hermite', 'bezier', 'save' ]

def parse_file( fname, edges, transform, screen, color ):
     f = open(fname)
     lines = f.readlines()

     c = 0
     while c < len(lines):
          line = lines[c].strip()
          #print ':' + line + ':'

          if line in ARG_COMMANDS:
               c+= 1
               args = lines[c].strip().split(' ')

          if line == 'line':
               #print 'LINE\t' + str(args)
               add_edge( edges,
                      int(args[0]), int(args[1]), int(args[2]),
                      int(args[3]), int(args[4]), int(args[5]) )

          elif line == 'scale':
               #print 'SCALE\t' + str(args)
               t = make_scale(int(args[0]), int(args[1]), int(args[2]))
               matrix_mult(t, transform)

          elif line == 'move':
               #print 'MOVE\t' + str(args)
               t = make_translate(int(args[0]), int(args[1]), int(args[2]))
               matrix_mult(t, transform)

          elif line == 'rotate':
               #print 'ROTATE\t' + str(args)
               theta = int(args[1]) * (math.pi / 180)

               if args[0] == 'x':
                    t = make_rotX(theta)
               elif args[0] == 'y':
                    t = make_rotY(theta)
               else:
                    t = make_rotZ(theta)
               matrix_mult(t, transform)

          elif line == 'circle':
               add_circle(edges, int(args[0]), int(args[1]), args[2], int(args[3]), 0.05)

          elif line == 'hermite':
               add_hermite(edges, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6]), int(args[7]), 0.05)
          elif line == 'bezier':
               add_bezier(edges, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6]), int(args[7]), 0.05)
          elif line == 'ident':
               ident(transform)

          elif line == 'apply':
               matrix_mult( transform, edges )

          elif line == 'display' or line == 'save':
               clear_screen(screen)
               draw_lines(edges, screen, color)

               if line == 'display':
                    display(screen)
               else:
                    save_extension(screen, args[0])
          elif line == 'box':
               add_box(edges, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
          elif line == 'sphere':
               add_sphere(edges, int(args[0]), int(args[1]), int(args[2]), int(args[3]), 0.01)
          elif line == 'torus':
               #add_torus
               add_torus(edges, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), 0.01)
          
          c+= 1
