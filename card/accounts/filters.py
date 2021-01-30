import django_filters
from .models import *

class naive_userFilter(django_filters.FilterSet):
	class Meta:
		model = naive_user
		fields = '__all__'