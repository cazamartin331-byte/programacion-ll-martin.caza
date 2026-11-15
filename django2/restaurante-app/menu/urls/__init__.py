from .categoria_urls import urlpatterns as categoria_patterns
from .home_urls import urlpatterns as home_patterns
from .ingrediente_urls import urlpatterns as ingrediente_patterns
from .plato_urls import urlpatterns as plato_patterns

urlpatterns = (home_patterns + plato_patterns
               + categoria_patterns + ingrediente_patterns)
