from django.db import models
import uuid
from pgvector.django import VectorField
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Documents(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_id = models.IntegerField()
    chunk_id = models.IntegerField()
    clean_text = models.TextField()
    tags = ArrayField(models.TextField())
    embedding = VectorField(
        dimensions=384,
        help_text="Vector embeddings generated using MiniLM-L6-v2",
    )

    def __str__(self):
        return f"Document UID: {self.document_id}"
