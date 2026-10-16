# Sistema de Biblioteca (Django)

Aplicação web com CRUD completo de **Autores** e **Livros** (Livro → ForeignKey → Autor),
usando o padrão MTV do Django, templates HTML, formulários e mensagens de feedback.

## Como executar
```bash
python -m venv venv
venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Acesse: http://127.0.0.1:8000/

(Opcional) `python manage.py createsuperuser` para usar o /admin só como apoio.

## Estrutura
- `config/` – configurações do projeto (settings, urls)
- `biblioteca/models.py` – modelos Autor e Livro (ForeignKey)
- `biblioteca/views.py` – views do CRUD
- `biblioteca/urls.py` – rotas
- `biblioteca/forms.py` – formulários (ModelForm)
- `biblioteca/templates/biblioteca/` – templates HTML
- `db.sqlite3` – banco criado após `migrate`
