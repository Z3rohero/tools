from abc import ABC, abstractclassmethod
from PIL import Image
import mimetypes
from pdfminer.hight_level import extract_text
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


class  MetadataExtractor(ABC):
    @abstractclassmethod
    def extract(self, filepath):
        pass


class ImageMetadataExtractor(MetadataExtractor):
      def extract(self, filepath):
           with Image.open(filepath) as img:
                if img.format in ['JPG','JPEG']:
                     exif = img._getexif()
                     if exif:
                          return {Image.ExifTags.TAGS.get(key,key):value
                                  for key, value in exif.items() if key in Image.ExifTags.TAGS
                                  }
                     else:
                          return {"Error" : "No exif metadada found"}
                elif img.format in ['PNG']:
                     if img.info:
                          return img.info
                     else:
                          return {"Error" : "No metadata found"}
                else:
                     return {"Error"}

class PdfMetadataExtractor(MetadataExtractor):
     def extract(self,filepath):
          metadata = {}
          with open(filepath,'rb') as f:
               parser = PDFParser(f)
               doc =  PDFDocument(parser)
               if doc.info:
                    for info in doc.info:
                         for key, values in info.items():
                              if isinstance(values,bytes):
                                   try:
                                        #Intentar decodificarlo en UTF-16be
                                        decoded_value = value.decode('utf-16be')
                                    except UnicodeDecodeError:
                                        #Intentar decoodificarlo en UTF-8
                                        decode_value = value.decode('utf-8',errors='ignore')
                                         
    
class MetadataExtractorFactory:
     @staticmethod
     def get_extractor(filepath):
          mime_type, _ =  mimetypes.guess_type(filepath)
          if mime_type:
               if mime_type.startswith('image'):
                    return ImageMetadataExtractor()


def extract_metadata(filepath):
     extractor = MetadataExtractorFactory.get_extractor(filepath)
     return extractor.extract(filepath)
