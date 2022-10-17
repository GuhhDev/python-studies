from os import path
from PIL import Image, ImageEnhance

class Editor():
    img = None
    img_formato = None
    img_local = None
    img_nome = None
    img_ext = None
    
    def reset(self):
        self.img = None
        self.img_formato = None
        self.img_local = None
        self.img_nome = None
        self.img_ext = None
    
    def load_image(self, imagem):
        try:
            self.img = Image.open(imagem)
            self.img_formato = self.img.format
            self.img_local = path.dirname(path.realpath(imagem))
            self.img_nome, self.img_ext = path.splitext(path.basename(imagem))
            print('imagem carregada!')
            return True
        except:
            print('falha ao carregar imagem')
            return False
    
    def _spin_image(self, sentido='horario', angulo='90'):
        if (sentido == 'horario'):
            self.img = self.img.rotate(angulo * -1, expand=True)
        elif(sentido == 'anti_horario'):
            self.img = self.img.rotate(angulo, expand=True)
    
    def remove_color_image(self):
        converser = ImageEnhance.Color(self.img)
        self.img = converser.enhance(0)

    def save(self, local, name_image):
        ln = local + '/' + name_image + '.' + self.img_ext
        self.img.save(ln, self.img_formato)
        self.reset()

ed = Editor()
ed.load_image("gato.jpg")
ed.img.show()