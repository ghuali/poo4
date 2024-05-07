import re

class mikvoc:
    def __init__(self) -> None:
        pass 
        
    @staticmethod
    def buscar(texto: str) -> list:
        #patón de palabras que empiezan por vocal minúscula
        patron = "\\b[aeiou][^\\s.,]*"
        result = re.findall(patron, texto)
        return result
    

if __name__ == "__main__":
    text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vitae felis aliquet, gravida quam at, posuere libero. Maecenas sollicitudin nisi scelerisque, ultrices purus fringilla, convallis orci. Etiam luctus non nisl tempus lobortis. Suspendisse non consectetur velit. Cras volutpat eleifend nunc ut euismod. Nulla pulvinar nisi sed nibh luctus fermentum. Vestibulum metus lectus, lacinia sed consectetur non, accumsan sed arcu. Nulla aliquet efficitur mauris in aliquam. Morbi mattis faucibus odio id pulvinar. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam nec finibus tortor. Etiam suscipit porta leo, sed blandit velit sagittis ut. Vestibulum et consectetur urna, sed dapibus urna. Aliquam erat volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
            Proin ac ullamcorper sem. Suspendisse elementum fringilla leo. Maecenas eu sodales urna. Phasellus ullamcorper, mi at semper mattis, leo lectus suscipit leo, eu tristique mauris tortor vel ex. In id felis at elit auctor ultrices. Curabitur rutrum massa at massa scelerisque, suscipit feugiat elit eleifend. Proin in neque sit amet lectus fermentum egestas.

            Vestibulum quis purus magna. Integer condimentum orci at felis facilisis consequat id iaculis lacus. Fusce ut scelerisque neque. Nam in nisi ut nulla posuere convallis sagittis a tellus. Phasellus erat lorem, porttitor at elit et, congue maximus risus. Aenean ut ligula facilisis, tristique enim nec, elementum nunc. Sed laoreet, arcu vel ultricies tincidunt, lacus ante ornare tellus, vel fermentum diam nibh vel nisi. Vivamus consectetur, eros sit amet venenatis faucibus, massa justo sodales eros, ut aliquam ipsum dolor ac metus.

Suspendisse laoreet eros enim, sed tempor ex consectetur eu. Nullam euismod tincidunt efficitur. Morbi id fermentum sapien, eu bibendum lacus. Vestibulum feugiat aliquet posuere. Vestibulum at felis a arcu placerat consequat at vitae elit. Nulla congue, enim in dictum rutrum, elit magna feugiat magna, nec congue magna libero eu lorem. Nullam sagittis, libero non condimentum pharetra, eros ligula ullamcorper sem, sit amet porta nulla nisi ut lectus. Vivamus condimentum dignissim erat, sit amet varius arcu consequat eget. Vestibulum molestie arcu lacus, ac luctus sapien fringilla sit amet. Vivamus aliquam vel dolor eget fermentum. Phasellus nec vestibulum sem, sit amet rutrum odio. Vivamus lacinia turpis eu porttitor fermentum. Donec dolor ligula, volutpat at metus vel, venenatis efficitur odio.

Proin ligula urna, fermentum sed lorem non, ultricies sollicitudin lorem. Nam rutrum ligula at lorem vulputate tristique. Sed aliquet ante non cursus accumsan. Nam molestie maximus porta. Nunc non sodales magna. Sed quam nunc, elementum in mattis sed, luctus at quam. Aenean aliquam dui eu purus luctus venenatis. In arcu est, interdum sed tellus at, mollis pellentesque tellus. Integer et ornare risus, pretium interdum enim. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse commodo ultricies urna, sit amet gravida erat finibus gravida. Cras sed iaculis purus. Vivamus facilisis magna vel nibh hendrerit, et commodo massa fringilla."""
    
    print(mikvoc.buscar(text))