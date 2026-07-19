from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_first_name(self):
        return self.cleaned_data["first_name"].strip()

    def clean_last_name(self):
        return self.cleaned_data["last_name"].strip()

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        if password1:
            user = User(
                username=cleaned_data.get("username", ""),
                email=cleaned_data.get("email", ""),
                first_name=cleaned_data.get("first_name", ""),
                last_name=cleaned_data.get("last_name", ""),
            )
            try:
                validate_password(password1, user=user)
            except ValidationError as error:
                self.add_error("password1", error)

        return cleaned_data

    def save(self):
        data = self.cleaned_data
        return User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password1"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        )


class AdminInviteUserForm(UserRegistrationForm):
    is_active = forms.BooleanField(required=False, initial=True, label="Active account")
    is_staff = forms.BooleanField(required=False, initial=False, label="Staff access")

    def save(self):
        user = super().save()
        user.is_active = self.cleaned_data.get("is_active", False)
        user.is_staff = self.cleaned_data.get("is_staff", False)
        user.save(update_fields=["is_active", "is_staff"])
        return user


class BaseLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    error_message = "Invalid username or password."

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.user = None

    def clean_username(self):
        return self.cleaned_data["username"].strip()

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            self.user = authenticate(self.request, username=username, password=password)
            if self.user is None:
                raise ValidationError(self.error_message)

        return cleaned_data

    def get_user(self):
        return self.user


class UserLoginForm(BaseLoginForm):
    def clean(self):
        cleaned_data = super().clean()
        if self.user and (self.user.is_staff or self.user.is_superuser):
            raise ValidationError("Please use the administrator login page.")
        return cleaned_data


class AdminLoginForm(BaseLoginForm):
    def clean(self):
        cleaned_data = super().clean()
        if self.user and not (self.user.is_staff and self.user.is_superuser):
            raise ValidationError("Permission denied. Superuser access is required.")
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

    def clean_first_name(self):
        return self.cleaned_data["first_name"].strip()

    def clean_last_name(self):
        return self.cleaned_data["last_name"].strip()

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if User.objects.filter(username__iexact=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Email already exists.")
        return email


class AdminProfileForm(UserProfileForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
