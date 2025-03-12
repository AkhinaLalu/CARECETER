document.addEventListener("DOMContentLoaded", function () {
    let flashError = "<?= $this->session->flashdata('error') ?>";
    let flashSuccess = "<?= $this->session->flashdata('success') ?>";
    let flashMessage = "<?= $this->session->flashdata('msg') ?>";
    let baseUrl = "<?= base_url() ?>";
    
    if (flashError) {
        Swal.fire("Error!", flashMessage, "error");
    }
    
    if (flashSuccess) {
        Swal.fire({
            title: "Member Registered Successfully!",
            text: flashMessage,
            imageUrl: baseUrl + "images/mee.png",
            confirmButtonColor: "#dc3545"
        });
    }

    // Form validation values
    let validationErrors = "<?= validation_errors() ?>";
    if (validationErrors) {
        console.log("Validation Errors:", validationErrors);
        
        let formData = {
            member_id: "<?= set_value('member_id') ?>",
            headoffice_id: "<?= set_value('headoffice_id') ?>",
            refered_by: "<?= set_value('refered_by') ?>",
            member_type_id: "<?= set_value('member_type_id') ?>",
            prefix: "<?= set_value('prefix') ?>",
            name: "<?= set_value('name') ?>",
            gst_no: "<?= set_value('gst_no') ?>",
            address: "<?= set_value('address') ?>",
            husband: "<?= set_value('husband') ?>",
            dob: "<?= set_value('dob') ?>",
            email: "<?= set_value('email') ?>",
            dom: "<?= set_value('dom') ?>",
            aadhar: "<?= set_value('aadhar') ?>",
            surname: "<?= set_value('surname') ?>",
            phone: "<?= set_value('phone') ?>",
            pincode: "<?= set_value('pincode') ?>",
            current_parish: "<?= set_value('current_parish') ?>",
            children: "<?= set_value('children') ?>",
            category: "<?= set_value('category') ?>",
            district_id: "<?= set_value('district_id') ?>",
            remark: "<?= set_value('remark') ?>",
            blood_group: "<?= set_value('blood_group') ?>",
            prayer_group_id: "<?= set_value('prayer_group_id') ?>",
            father_name: "<?= set_value('father_name') ?>",
            occupation: "<?= set_value('occupation') ?>",
            organization: "<?= set_value('organization') ?>",
            status: "<?= set_checkbox('status', 1) ?>",
            files: "<?= json_encode(set_value('files')) ?>",
            members: {
                member_name: "<?= json_encode(set_value('member[member_name][]')) ?>",
                member_relation: "<?= json_encode(set_value('member[member_relation][]')) ?>",
                member_profession: "<?= json_encode(set_value('member[member_profession][]')) ?>",
                member_dob: "<?= json_encode(set_value('member[member_dob][]')) ?>",
                member_dom: "<?= json_encode(set_value('member[member_dom][]')) ?>",
                member_mobile: "<?= json_encode(set_value('member[member_mobile][]')) ?>",
                member_blood_group: "<?= json_encode(set_value('member[member_blood_group][]')) ?>",
                member_files: "<?= json_encode(set_value('member[member_files][]')) ?>"
            }
        };

        console.log("Form Data:", formData);
    }
});