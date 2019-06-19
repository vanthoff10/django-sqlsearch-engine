from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import FormData, DataSchema


# Create your views here.
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1buqR2OkUJdPA63NYh2WZWRoCQ4-P_8JP-7vogko3oYA'
SAMPLE_RANGE_NAME = 'A3:F'
SAMPLE_RANGE_GREG = 'G3:L'
SAMPLE_RANGE_KEVIN = 'M3:R'
SAMPLE_RANGE_MATT = 'S3:X'
SAMPLE_RANGE_ORG = 'Y3:AD'
SAMPLE_RANGE_ECLIENTS = 'AE3:AF'


def index(request):
    return render(request)


def create(request):
    if request.method == "POST":
        input_text = request.POST['search']
        value_text = request.POST['prodId']
        all_data = DataSchema.objects.filter(company_name__icontains=input_text).values('company_name', 'company_url', 'company_email', 'f_name', 'l_name', 'city_name')
        if all_data:
            return TemplateResponse(request, 'home.html', {'data': all_data})
        else:
            return TemplateResponse(request, 'home.html', {'data_value': value_text})


def savedata(request):
    if request.method == "POST":

        form_data_obj = FormData()
        dataschema_obj = DataSchema()

        datafield1 = request.POST['data1']
        datafield2 = request.POST['data2']
        datafield3 = request.POST['data3']
        datafield4 = request.POST['data4']
        datafield5 = request.POST['data5']
        datafield6 = request.POST['data6']
        datafield7 = request.POST['data7']
        datafield8 = request.POST['data8']
        datafield9 = request.POST['data9']
        datafield10 = request.POST['data10']
        datafield11 = request.POST['data11']
        datafield12 = request.POST['data12']
        datafield13 = request.POST['data13']
        datafield14 = request.POST['data14']
        datafield15 = request.POST['data15']
        datafield16 = request.POST['data16']

        # Form info save to users_formdata DB

        form_data_obj.lead_gen = datafield1
        form_data_obj.company_name = datafield2
        form_data_obj.company_address = datafield3
        form_data_obj.company_city = datafield4
        form_data_obj.company_state = datafield5
        form_data_obj.company_country = datafield6
        form_data_obj.company_url = datafield7
        form_data_obj.company_linkedin = datafield8
        form_data_obj.company_phone = datafield9
        form_data_obj.company_email = datafield10
        form_data_obj.f_name = datafield11
        form_data_obj.l_name = datafield12
        form_data_obj.owner_linkedin = datafield13
        form_data_obj.owner_title = datafield14

        # Form info save to users_formdata DB
        dataschema_obj.company_name = datafield2
        dataschema_obj.company_url = datafield7
        dataschema_obj.company_email = datafield10
        dataschema_obj.f_name = datafield11
        dataschema_obj.l_name = datafield12
        dataschema_obj.city_name = datafield4

        form_data_obj.save()
        dataschema_obj.save()

        return TemplateResponse(request, 'home.html')


def main(request):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()

    # for greg
    result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_GREG).execute()

    # for kevin
    result3 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_KEVIN).execute()

    # for matt
    result4 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_MATT).execute()

    # for organizations
    result5 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_ORG).execute()

    # for existing clients
    result6 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_ECLIENTS).execute()

    values = result.get('values', [])
    values_greg = result2.get('values', [])
    values_kevin = result3.get('values', [])
    values_matt = result4.get('values', [])
    values_org = result5.get('values', [])
    values_eclients = result6.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Fetching Data of GABE from DB')

        for row in values:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_kevin:
        print('No data found.')
    else:
        print('Fetching Data of GREG from DB')

        for row in values_kevin:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_greg:
        print('No data found.')
    else:
        print('Fetching Data of KEVIN from DB')

        for row in values_greg:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_matt:
        print('No data found.')
    else:
        print('Fetching Data of MATT from DB')

        for row in values_matt:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_org:
        print('No data found.')
    else:
        print('Fetching Data of ORGANIZATIONS from DB')

        for row in values_org:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_url = row[1]
                    sheetdata_obj.company_email = row[2]
                    sheetdata_obj.f_name = row[3]
                    sheetdata_obj.l_name = row[4]
                    sheetdata_obj.city_name = row[5]
            except IndexError:
                pass

            sheetdata_obj.save()

    if not values_eclients:
        print('No data found.')
    else:
        print('Fetching Data of EXISTING CLIENTS from DB')

        for row in values_eclients:
            sheetdata_obj = DataSchema()
            try:
                if row:
                    sheetdata_obj.company_name = row[0]
                    sheetdata_obj.company_email = row[1]
            except IndexError:
                pass

            sheetdata_obj.save()

    return TemplateResponse(request, 'home.html', {'info': values_greg})


