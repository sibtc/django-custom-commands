from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Show all available styles'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.ERROR('error - A major error.'))
        self.stdout.write(self.style.NOTICE('notice - A minor error.'))
        self.stdout.write(self.style.SUCCESS('success - A success.'))
        self.stdout.write(self.style.WARNING('warning - A warning.'))
        self.stdout.write(self.style.SQL_FIELD('sql_field - The name of a model field in SQL.'))
        self.stdout.write(self.style.SQL_COLTYPE('sql_coltype - The type of a model field in SQL.'))
        self.stdout.write(self.style.SQL_KEYWORD('sql_keyword - An SQL keyword.'))
        self.stdout.write(self.style.SQL_TABLE('sql_table - The name of a model in SQL.'))
        self.stdout.write(self.style.HTTP_INFO('http_info - A 1XX HTTP Informational server response.'))
        self.stdout.write(self.style.HTTP_SUCCESS('http_success - A 2XX HTTP Success server response.'))
        self.stdout.write(self.style.HTTP_NOT_MODIFIED('http_not_modified - A 304 HTTP Not Modified server response.'))
        self.stdout.write(self.style.HTTP_REDIRECT('http_redirect - A 3XX HTTP Redirect server response other than 304.'))
        self.stdout.write(self.style.HTTP_NOT_FOUND('http_not_found - A 404 HTTP Not Found server response.'))
        self.stdout.write(self.style.HTTP_BAD_REQUEST('http_bad_request - A 4XX HTTP Bad Request server response other than 404.'))
        self.stdout.write(self.style.HTTP_SERVER_ERROR('http_server_error - A 5XX HTTP Server Error response.'))
        self.stdout.write(self.style.MIGRATE_HEADING('migrate_heading - A heading in a migrations management command.'))
        self.stdout.write(self.style.MIGRATE_LABEL('migrate_label - A migration name.'))
