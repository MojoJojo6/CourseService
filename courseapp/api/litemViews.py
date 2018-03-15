"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import generics
from courseapp.models import Litem
from .litemSerializers import LitemSerializerCUD, LitemSerializerR

class LitemCreate(generics.CreateAPIView):
    serializer_class = LitemSerializerCUD
    queryset = Litem.objects.all()

class LitemList(generics.ListAPIView):
    serializer_class = LitemSerializerR
    queryset = Litem.objects.all()
    # def get_queryset(self):
    #     queryset = Litem.objects.all()
    #     query_params = self.request.query_params
    #     lesson_id = query_params.get('lid', None)
    #     litem_seqnum = query_params.get('seqnum', None)

        # if lesson_id != None and litem_seqnum != None:
        #     """
        #     Retrieve list of lesson items by `lesson_id` and `litem_seqnum`
        #
        #     To get the litem with given sequence number under a lesson.
        #     It is useful when user wants to load a specific lesson item by its sequence number.
        #     """
        #     return Litem.objects.filter(lesson=lesson_id, litem_seqnum=litem_seqnum)
        # elif lesson_id != None:
        #     """
        #     Retrieve list of lesson items by `lesson_id`
        #
        #     To get the list of all the lesson items associated with same lesson.
        #     It is useful when user wants to load a lesson item playlist.
        #     """
        #     return Litem.objects.filter(lesson=lesson_id)
        # else:
        #     """
        #     Get list of all the lessons (irrespective of course)
        #     """
        #     return Litem.objects.all()


class LitemRUDView(generics.RetrieveUpdateDestroyAPIView):
    # serializer_class = LitemSerializer
    queryset = Litem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            import pdb
            pdb.set_trace()

            return LitemSerializerR
        elif self.request.method == "PUT" or "PATCH" or "DELETE":
            return LitemSerializerCUD
