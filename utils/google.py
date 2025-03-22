from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleDocClient:
    """
    Wrapper for Google Docs operations, really just auth and retrieval for now

    Args:
        - service_account_json (str): Filepath pointing to a Service Account credentials JSON file
        - scopes (list): List of scopes allowed for this client
    """

    def __init__(self, service_account_json: str, scopes: list):
        self.service_account_json = service_account_json
        self.scopes = scopes
        self.credentials = self._authenticate()
        self.google_docs = self._build_service()

    def _authenticate(self):
        """
        Internal method to generate GoogleAPI credentials object
        """
        credentials = service_account.Credentials.from_service_account_file(
            self.service_account_json, scopes=self.scopes
        )
        return credentials

    def _build_service(self):
        """
        Build an accessible Google Docs service for use in Python
        """
        service = build("docs", "v1", credentials=self.credentials)
        return service

    def fetch_document(self, document_id: str) -> dict:
        """
        Given a document ID, retrieve the associated document

        Args:
            - document_id (srt): Document ID for document of interest (alphanumeric code following "d/" in document link)

        Returns:
            - response (dict): JSON response from Google API
        """

        response = self.google_docs.documents().get(documentId=document_id).execute()
        return response

    def extract_text(self, google_doc_repsonse: dict) -> str:
        """
        Given a Google API response, extract the text from the document

        Args:
            - google_doc_repsonse (dict): Response from Google Docs API

        Returns:
            - document_text (str): Text from within document
        """
        document_text = ""
        for element in google_doc_repsonse.get("body").get("content"):
            if "paragraph" in element:
                for paragraph in element["paragraph"].get("elements", []):
                    if "textRun" in paragraph:
                        document_text += paragraph["textRun"]["content"]
        return document_text
