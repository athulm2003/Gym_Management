import streamlit as st
from gymviews import GymMemberManager

member_instance=GymMemberManager()

tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Member ")
    name=st.text_input("Enter Member Name")
    place=st.text_input("Enter  Place")
    mobile=st.text_input("Enter Phone Number")
    plan=st.selectbox("Select Membership plan",['1 month','3 month','6 month','1 year'])
    fee=st.text_input("Enter the Fee Amount")
    joined_date=st.date_input("Enter Joined_date (yyyy/mm/dd)")
    if st.button("Add New Member"):
        member_instance.post(name=name,place=place,mobile=mobile,plan=plan,fee=fee,joined_date=joined_date)
        st.success("New Member Added Successfully")


with tab2:
    st.title("View Member Details")
    records=member_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No records found...!")


