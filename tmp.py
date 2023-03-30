# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProfileProfiledata(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    sex = models.CharField(max_length=5)
    age = models.IntegerField()
    info = models.CharField(max_length=128)
    delete_flag = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Profile_profiledata'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AccountInfo(models.Model):
    id = models.UUIDField(primary_key=True)
    user_name = models.CharField(max_length=60)
    account = models.CharField(unique=True, max_length=60)
    password = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account_info'


class AppItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_item'


class AppOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField()
    user_id = models.BigIntegerField()
    payment = models.ForeignKey('AppPayment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_order'


class AppOrderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(AppOrder, models.DO_NOTHING)
    orderitem = models.ForeignKey('AppOrderitem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_order_items'
        unique_together = (('order', 'orderitem'),)


class AppOrderitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    ordered = models.BooleanField()
    quantity = models.IntegerField()
    item = models.ForeignKey(AppItem, models.DO_NOTHING)
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'app_orderitem'


class AppPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.IntegerField()
    timestamp = models.DateTimeField()
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_payment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class IncomeforecastIncomeforecastdata(models.Model):
    income_forecast_id = models.UUIDField(primary_key=True)
    payment_date = models.DateField()
    age = models.CharField(max_length=5)
    industry = models.CharField(max_length=120)
    total_amount = models.IntegerField()
    deduction_amount = models.IntegerField()
    take_home_amount = models.IntegerField(blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    classification = models.CharField(max_length=20)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'incomeforecast_incomeforecastdata'


class JapanannualincomeIncomedata(models.Model):
    income_id = models.UUIDField(primary_key=True)
    company_name = models.CharField(max_length=60)
    company_size = models.CharField(max_length=20)
    industry = models.CharField(max_length=120)
    employee_number = models.IntegerField()
    avg_age = models.IntegerField()
    avg_income = models.IntegerField()
    delete_flag = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'japanannualincome_incomedata'


class JapanannualincomeUsereditinfo(models.Model):
    user = models.CharField(max_length=30)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'japanannualincome_usereditinfo'


class JobsJoboffer(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=254)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.SmallIntegerField()
    prefectures = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'jobs_joboffer'


class ObjectDetectionModel(models.Model):
    id = models.UUIDField(primary_key=True)
    project_name_id = models.IntegerField()
    object_detection_model_name = models.CharField(unique=True, max_length=20)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'object_detection_model'


class OriginsiteActor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'originsite_actor'


class PersonalinfoActor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_actor'


class PersonalinfoAddress(models.Model):
    address_id = models.CharField(primary_key=True, max_length=4)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('PersonalinfoCity', models.DO_NOTHING)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=-1)
    staff_id = models.CharField(max_length=-1)
    store_id = models.CharField(max_length=-1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_address'


class PersonalinfoCategory(models.Model):
    category_id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_category'


class PersonalinfoCity(models.Model):
    city_id = models.CharField(primary_key=True, max_length=4)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('PersonalinfoCountry', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_city'


class PersonalinfoCountry(models.Model):
    country_id = models.CharField(primary_key=True, max_length=4)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_country'


class PersonalinfoCustomer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=4)
    store_id = models.CharField(max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(PersonalinfoAddress, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personalinfo_customer'
        unique_together = (('customer_id', 'store_id', 'address', 'last_name'),)


class PersonalinfoFilmActor(models.Model):
    actor = models.OneToOneField(PersonalinfoActor, models.DO_NOTHING, primary_key=True)
    film_id = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_film_actor'
        unique_together = (('actor', 'film_id'),)


class PersonalinfoFilmCategory(models.Model):
    film_id = models.CharField(primary_key=True, max_length=8)
    category = models.ForeignKey(PersonalinfoCategory, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_film_category'
        unique_together = (('film_id', 'category'),)


class PersonalinfoFilmText(models.Model):
    film_id = models.CharField(primary_key=True, max_length=4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_film_text'


class PersonalinfoFilms(models.Model):
    film_id = models.CharField(primary_key=True, max_length=4)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('PersonalinfoLanguages', models.DO_NOTHING)
    rental_duration = models.CharField(max_length=8)
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    lengths = models.CharField(max_length=8, blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=32, blank=True, null=True)
    special_features = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_films'
        unique_together = (('film_id', 'title', 'language'),)


class PersonalinfoInventory(models.Model):
    inventory_id = models.CharField(primary_key=True, max_length=4)
    film_id = models.CharField(max_length=4)
    store_id = models.CharField(max_length=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_inventory'
        unique_together = (('inventory_id', 'film_id', 'store_id'),)


class PersonalinfoLanguages(models.Model):
    language_id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_languages'


class PersonalinfoPayment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=8)
    customer_id = models.CharField(max_length=8)
    staff_id = models.CharField(max_length=8)
    rental_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_payment'
        unique_together = (('payment_id', 'staff_id', 'customer_id'),)


class PersonalinfoRental(models.Model):
    rental_id = models.CharField(primary_key=True, max_length=8)
    rental_date = models.DateTimeField()
    inventory_id = models.CharField(max_length=8)
    customer_id = models.CharField(max_length=8)
    return_date = models.DateTimeField(blank=True, null=True)
    staff_id = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_rental'
        unique_together = (('rental_id', 'rental_date', 'inventory_id', 'customer_id'),)


class PersonalinfoStaff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(PersonalinfoAddress, models.DO_NOTHING)
    picture = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.CharField(max_length=4)
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_staff'
        unique_together = (('staff_id', 'store_id', 'address'),)


class PersonalinfoStore(models.Model):
    store_id = models.CharField(primary_key=True, max_length=4)
    manager_staff_id = models.CharField(max_length=4)
    address = models.ForeignKey(PersonalinfoAddress, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'personalinfo_store'
        unique_together = (('store_id', 'manager_staff_id', 'address'),)


class ProfileActor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profile_actor'


class Project(models.Model):
    id = models.UUIDField(primary_key=True)
    object_detection_model_name_id = models.IntegerField()
    project_name = models.CharField(max_length=20)
    delete_flag = models.IntegerField()
    update_user = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class StockpriceforecastBrand(models.Model):
    brand = models.CharField(max_length=60)
    delete_flag = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stockpriceforecast_brand'


class StockpriceforecastStockpriceforecast(models.Model):
    stock_price_date = models.DateField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    delete_flag = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    brand = models.ForeignKey(StockpriceforecastBrand, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stockpriceforecast_stockpriceforecast'


class UserinfoActor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userinfo_actor'


class UserinfoPulldownselect(models.Model):
    pulldown_name = models.CharField(max_length=128, blank=True, null=True)
    identification_number = models.IntegerField(blank=True, null=True)
    active_flag = models.IntegerField(blank=True, null=True)
    list_num = models.IntegerField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    created_at = models.TimeField()

    class Meta:
        managed = False
        db_table = 'userinfo_pulldownselect'


class UserinfoSampledata(models.Model):
    id = models.UUIDField(primary_key=True)
    param_id = models.CharField(max_length=128, blank=True, null=True)
    sample1 = models.CharField(max_length=128)
    sample2 = models.CharField(max_length=128)
    code1 = models.IntegerField(blank=True, null=True)
    code2 = models.IntegerField(blank=True, null=True)
    code3 = models.IntegerField(blank=True, null=True)
    code4 = models.IntegerField(blank=True, null=True)
    sample3 = models.CharField(max_length=128, blank=True, null=True)
    sample4 = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userinfo_sampledata'


class UserinfoUserinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    sex = models.CharField(max_length=128)
    age = models.IntegerField()
    info = models.CharField(max_length=128)
    hobby = models.CharField(max_length=128)
    created_at = models.TimeField()

    class Meta:
        managed = False
        db_table = 'userinfo_userinfo'
