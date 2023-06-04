import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)


def code_generator(size = SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
	
def create_shortcode(instance, size=SHORTCODE_MIN):
	newc = code_generator(size=size)
	Klass = instance.__class__
	qs = Klass.objects.filter(shortcode=newc).exists()
	if qs:
		return create_shortcode(size=size)
	return newc