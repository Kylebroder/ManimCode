from manim import *
import numpy as np

class Bigger(Scene):
	def construct(self):
		t1 = MathTex(r"\text{Which is bigger,}").scale(3)\
			.to_edge(UP)\
			.set_color_by_gradient(BLUE, GREEN)

		self.play(Write(t1))

		self.wait(1)

		t1A = MathTex(r"2^{300}\ \ \text{or} \ \ 3^{200} ?").scale(4)\
			.next_to(t1,DOWN)\
			.shift(DOWN)

		self.play(FadeInFrom(t1A,DOWN))

# 		self.wait(6)

# 		t1B = MathTex(r"\text{Write}").scale(0.8)\
# 			.next_to(t1A,DOWN)\
# 			.to_corner(LEFT)\
# 			.shift(DOWN*0.5)

# 		self.play(Write(t1B))

# 		self.wait(2)

# 		t1C = MathTex(r"2^{300} = 2^{3 \cdot 100}", color = GOLD_B).scale(0.8)\
# 			.next_to(t1B,RIGHT)

# 		self.play(Write(t1C))

# 		self.wait(2)

# 		t1D = MathTex(r"= (2^3)^{100}", color = GOLD_B).scale(0.8)\
# 			.next_to(t1C,RIGHT)

# 		self.play(Write(t1D))

# 		self.wait(2)

# 		t1E = MathTex(r"= 8^{100},", color = GOLD_B).scale(0.8)\
# 			.next_to(t1D,RIGHT)

# 		self.play(Write(t1E))

# 		self.wait(2)

# 		t2 = MathTex(r"\text{and}").scale(0.8)\
# 			.next_to(t1B,DOWN)\
# 			.shift(RIGHT*5)

# 		t2A = MathTex(r"3^{200} = 3^{2 \cdot 100}", color = RED_B).scale(0.8)\
# 			.next_to(t2,RIGHT)

# 		self.play(Write(t2))

# 		self.wait(2)

# 		self.play(Write(t2A))

# 		self.wait(2)

# 		t2B = MathTex(r"= (3^2)^{100}", color = RED_B).scale(0.8)\
# 			.next_to(t2A,RIGHT)

# 		self.play(Write(t2B))

# 		self.wait(2)

# 		t2C = MathTex(r"= 9^{100}", color = RED_B).scale(0.8)\
# 			.next_to(t2B,RIGHT)

# 		self.play(Write(t2C))

# 		self.wait(2)

# 		t3 = MathTex(r"\ \implies \ 2^{300} = 8^{100}", color = PINK).scale(0.8)\
# 			.shift(LEFT*2)

# 		self.play(Write(t3))

# 		self.wait(6)

# 		t3A = MathTex(r"< 9^{100} = 3^{200}.", color = PINK).scale(0.8)\
# 			.next_to(t3,RIGHT)

# 		self.play(Write(t3A))

# 		self.wait(1)

# class Lachie(Scene):
# 	def construct(self):

# 		t1 = MathTex(r"\text{This problem was brought to my attention}").scale(0.7)\
# 			.shift(UP*1.5)

# 		t1A = MathTex(r"\text{by Lachlan Oberg}.").scale(0.7)\
# 			.next_to(t1,DOWN)

# 		t1.add(t1A)


# 		self.play(FadeInFrom(t1,DOWN))

# 		self.wait(4)


