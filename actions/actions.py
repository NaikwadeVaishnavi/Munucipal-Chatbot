from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionUtterGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")
        return []

class ActionUtterGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_goodbye")
        return []

class ActionUtterAffirm(Action):
    def name(self) -> Text:
        return "utter_affirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_affirm")
        return []

class ActionUtterDeny(Action):
    def name(self) -> Text:
        return "utter_deny"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_deny")
        return []

class ActionUtterBotChallenge(Action):
    def name(self) -> Text:
        return "utter_bot_challenge"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_bot_challenge")
        return []

class ActionProvideSOPStreetLights(Action):
    def name(self) -> Text:
        return "utter_street_lights"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_street_lights")
        return []

class ActionProvideSOPStreetDogs(Action):
    def name(self) -> Text:
        return "utter_street_dogs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_street_dogs")
        return []

class ActionProvideSOPCleanliness(Action):
    def name(self) -> Text:
        return "utter_cleanliness"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_cleanliness")
        return []

class ActionProvideSOPWaterManagement(Action):
    def name(self) -> Text:
        return "utter_water_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_water_management")
        return []

class ActionProvideSOPRoadMaintenance(Action):
    def name(self) -> Text:
        return "utter_road_maintenance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_road_maintenance")
        return []

class ActionProvideSOPWasteManagement(Action):
    def name(self) -> Text:
        return "utter_waste_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_waste_management")
        return []

class ActionProvideSOPCouncilTaxes(Action):
    def name(self) -> Text:
        return "utter_council_taxes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_council_taxes")
        return []

class ActionProvideSOPViolation(Action):
    def name(self) -> Text:
        return "utter_violation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_violation")
        return []


class ActionProvideSOPHealthManagement(Action):
    def name(self) -> Text:
        return "utter_health_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_health_management")
        return []

class ActionProvideSOPFirePreventionMeasures(Action):
    def name(self) -> Text:
        return "utter_fire_prevention_measures"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_fire_prevention_measures")
        return []


class ActionProvideSOPDeathBodyManagement(Action):
    def name(self) -> Text:
        return "utter_death_body_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response=" utter_death_body_management")
        return []


class ActionProvideSOPOrphanage(Action):
    def name(self) -> Text:
        return "utter_orphanage"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_orphanage")
        return []

class ActionProvideSOPDeathBirthRegistration(Action):
    def name(self) -> Text:
        return "utter_death_birth_registration"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_death_birth_registration")
        return []

class ActionProvideSOPVaccine(Action):
    def name(self) -> Text:
        return "utter_vaccine"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_vaccine")
        return []

class ActionProvideSOPPrimarySchoolsHospitals(Action):
    def name(self) -> Text:
        return "utter_primary_schools_hospitals"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_primary_schools_hospitals")
        return []

class ActionProvideSOPParks(Action):
    def name(self) -> Text:
        return "utter_parks"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_parks")
        return []

class ActionProvideSOPCensus(Action):
    def name(self) -> Text:
        return "utter_census"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_census")
        return []

class ActionProvideSOPEmployeeManagement(Action):
    def name(self) -> Text:
        return "utter_employee_management"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_employee_management")
        return []

class ActionProvideSOPLibraries(Action):
    def name(self) -> Text:
        return "utter_libraries"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_libraries")
        return []

class ActionProvideSOPRenewalOldBuildings(Action):
    def name(self) -> Text:
        return "utter_renewal_old_buildings"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_renewal_old_buildings")
        return []

class ActionProvideSOPLegalIndustriesCulture(Action):
    def name(self) -> Text:
        return "utter_legal_industries_culture"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_legal_industries_culture")
        return []

class ActionProvideSOPElectricity(Action):
    def name(self) -> Text:
        return "utter_electricity"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_electricity")
        return []

class ActionProvideSOPElection(Action):
    def name(self) -> Text:
        return "utter_election"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_election")
        return []

class ActionProvideSOPNoti(Action):
    def name(self) -> Text:
        return "utter_notices"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_notices")
        return []

class ActionProvideSOPLandDistribution(Action):
    def name(self) -> Text:
        return "utter_land_distribution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_land_distribution")
        return []

class ActionProvideSOPGeneralInfoDuties(Action):
    def name(self) -> Text:
        return "utter_general_info_duties"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_general_info_duties")
        return []

class ActionProvideSOPGeneralInfoResponsibilities(Action):
    def name(self) -> Text:
        return "utter_general_info_responsibilities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_general_info_responsibilities")
        return []
        
class ActionProvideBasicMunicipalInfo(Action):
    def name(self) -> Text:
        return "utter_basic_municipal_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_basic_municipal_info")
        return []

class ActionUtterFallback(Action):
    def name(self) -> Text:
        return "utter_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I'm sorry, I didn't understand that.")
        return []
