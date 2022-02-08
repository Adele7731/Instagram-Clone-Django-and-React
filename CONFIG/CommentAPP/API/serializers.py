from rest_framework import serializers
from CommentAPP.models import ModelComment
from datetime import datetime

class SerializerCommentListByPost(serializers.ModelSerializer):
    user        = serializers.CharField(source="user.username")
    replies     = serializers.SerializerMethodField()
    createdDate = serializers.SerializerMethodField()

    def get_createdDate(self, obj):
        tarih = datetime.strftime(obj.createdDate, '%d/%m/%Y %H:%M:%S')
        return str(tarih)

    def get_replies(self, obj):
        if obj.any_children:
            return SerializerCommentListByPost(obj.children(),many=True).data

    class Meta:
        model  = ModelComment
        fields = ("user","text","createdDate","replies")


