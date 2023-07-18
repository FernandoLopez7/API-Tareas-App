from rest_framework import generics
from .models import Tarea, TareaAsignada, UsuarioTareas
from .serializers import TareaSerializer, TareaAsignadaSerializer

class TareaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        usuario_actual = self.request.query_params.get('usuario')
        user = UsuarioTareas.objects.filter(user_id=usuario_actual).values_list('id', flat=True).first()
        queryset = Tarea.objects.filter(usuario=user)
        return queryset

class TareaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaAsignadaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TareaAsignadaSerializer
    
    def get_queryset(self):
        usuario_actual = self.request.query_params.get('usuario')
        user = UsuarioTareas.objects.filter(user_id=usuario_actual).values_list('id', flat=True).first()
        queryset =  TareaAsignada.objects.filter(asignado_a=user).select_related('tarea')
        return queryset

# class TareaAsignadaList(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TareaAsignadaSerializer
    
#     def get_queryset(self):
#         usuario_actual = self.request.query_params.get('usuario')
#         user = UsuarioTareas.objects.filter(user_id=usuario_actual).values_list('id', flat=True).first()
#         tareas = Tarea.objects.filter(usuario=user).values('id')
#         queryset = TareaAsignada.objects.filter(tarea__in=tareas)
#         return queryset
    

class TareaAsignadaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TareaAsignada.objects.all()
    serializer_class = TareaAsignadaSerializer