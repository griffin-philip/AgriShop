from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, FarmerProfile, CustomerProfile
from django.contrib.auth.forms import AuthenticationForm

INDIAN_STATES = [
    ("", "----- Select State -----"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
]

class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(
    choices=User.ROLE_CHOICES,
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['role'].widget.attrs.update({
            'class': 'form-check-input'
        })



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'
        })


class FarmerProfileForm(forms.ModelForm):
    state = forms.ChoiceField(choices=INDIAN_STATES, required=True)
    district = forms.ChoiceField(choices=[("", "----- Select District -----")], required=True)

    class Meta:
        model = FarmerProfile
        fields = ['farm_name', 'phone', 'state', 'district', 'pincode']

        widgets = {
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        district_data = {
            "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Tirupati"],
            "Arunachal Pradesh": ["Tawang", "Itanagar", "Ziro", "Pasighat"],
            "Assam": ["Guwahati", "Dibrugarh", "Silchar", "Jorhat"],
            "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur"],
            "Chhattisgarh": ["Raipur", "Bilaspur", "Durg", "Korba"],
            "Goa": ["North Goa", "South Goa", "Panaji", "Margao"],
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
            "Haryana": ["Gurgaon", "Faridabad", "Panipat", "Ambala"],
            "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Solan"],
            "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro"],
            "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubli"],
            "Kerala": ["Thiruvananthapuram", "Kollam", "Pathanamthitta", "Ernakulam"],
            "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
            "Manipur": ["Imphal", "Thoubal", "Churachandpur", "Bishnupur"],
            "Meghalaya": ["Shillong", "Tura", "Jowai", "Nongpoh"],
            "Mizoram": ["Aizawl", "Lunglei", "Champhai", "Serchhip"],
            "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang"],
            "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Puri"],
            "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota"],
            "Sikkim": ["Gangtok", "Namchi", "Gyalshing", "Mangan"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem"],
            "Telangana": ["Hyderabad", "Warangal", "Karimnagar", "Nizamabad"],
            "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Kailasahar"],
            "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra"],
            "Uttarakhand": ["Dehradun", "Haridwar", "Nainital", "Haldwani"],
            "West Bengal": ["Kolkata", "Howrah", "Darjeeling", "Durgapur"]
        }

        if 'state' in self.data:
            state = self.data.get('state')
            districts = district_data.get(state, [])
            self.fields['district'].choices = [(d, d) for d in districts]
        elif self.instance.pk and self.instance.state:
            districts = district_data.get(self.instance.state, [])
            self.fields['district'].choices = [(d, d) for d in districts]


class CustomerProfileForm(forms.ModelForm):
    state = forms.ChoiceField(choices=INDIAN_STATES, required=True)
    district = forms.ChoiceField(choices=[("", "----- Select District -----")], required=True)
    
    class Meta:
        model = CustomerProfile
        fields = ['phone', 'state', 'district', 'pincode']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        district_data = {
            "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Tirupati"],
            "Arunachal Pradesh": ["Tawang", "Itanagar", "Ziro", "Pasighat"],
            "Assam": ["Guwahati", "Dibrugarh", "Silchar", "Jorhat"],
            "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur"],
            "Chhattisgarh": ["Raipur", "Bilaspur", "Durg", "Korba"],
            "Goa": ["North Goa", "South Goa", "Panaji", "Margao"],
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
            "Haryana": ["Gurgaon", "Faridabad", "Panipat", "Ambala"],
            "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala", "Solan"],
            "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro"],
            "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubli"],
            "Kerala": ["Thiruvananthapuram", "Kollam", "Pathanamthitta", "Ernakulam"],
            "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
            "Manipur": ["Imphal", "Thoubal", "Churachandpur", "Bishnupur"],
            "Meghalaya": ["Shillong", "Tura", "Jowai", "Nongpoh"],
            "Mizoram": ["Aizawl", "Lunglei", "Champhai", "Serchhip"],
            "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang"],
            "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Puri"],
            "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota"],
            "Sikkim": ["Gangtok", "Namchi", "Gyalshing", "Mangan"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Salem"],
            "Telangana": ["Hyderabad", "Warangal", "Karimnagar", "Nizamabad"],
            "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Kailasahar"],
            "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra"],
            "Uttarakhand": ["Dehradun", "Haridwar", "Nainital", "Haldwani"],
            "West Bengal": ["Kolkata", "Howrah", "Darjeeling", "Durgapur"]
        }

        if 'state' in self.data:
            state = self.data.get('state')
            districts = district_data.get(state, [])
            self.fields['district'].choices = [(d, d) for d in districts]
        elif self.instance.pk and self.instance.state:
            districts = district_data.get(self.instance.state, [])
            self.fields['district'].choices = [(d, d) for d in districts]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
