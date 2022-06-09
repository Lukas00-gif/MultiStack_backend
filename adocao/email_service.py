from django.core.mail import send_mail

def enviar_email_confirmaçao(adocao):
    assunto = "Adoção Realizada com Sucesso"
    conteudo = f'Parabens por realizar o pet{adocao.pet.nome} com o valor mensal de {adocao.valor}'
    remetente = 'adoteumpet123teste@gmail.com'
    destinatario = [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)
    
