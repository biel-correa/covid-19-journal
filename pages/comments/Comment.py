from nanoid import generate

from pages.formError.FormError import FormError

class Comment:
    def __init__(self, name, email, content):
        self.id = generate()
        self.name = name
        self.email = email
        self.content = content
    
    @classmethod
    def validateData(self, data):
        errors = []
        if data['name'] == '':
            errors.append(FormError('name-error', 'Name is required'))
        if data['email'] == '':
            errors.append(FormError('email-error', 'Email is required'))
        if data['content'] == '':
            errors.append(FormError('content-error', 'Content is required'))
        return errors
