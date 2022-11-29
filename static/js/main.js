const addButton = document.querySelector('#add-row')
const deleteButton = document.querySelector('#delete-row')
const tbody = document.querySelector('#form-body')
const formRegex = RegExp(`product_line-(\\d){1}-`,'g')
let totalForms = document.querySelector("#id_product_line-TOTAL_FORMS")


const addForm = (e) => {
    e.preventDefault()

    const forms = document.querySelectorAll('.form')
    let formNum = forms.length - 1
    const newForm = forms[0].cloneNode(true)

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `product_line-${formNum}-`)
    console.log(newForm)
    newForm.firstElementChild.innerHTML = formNum + 1
    tbody.appendChild(newForm)

    totalForms.setAttribute('value', `${formNum + 1}`)
}

const deleteForm = (e) => {
    e.preventDefault()

    const forms = document.querySelectorAll('.form')

    e.target.parentNode.parentNode.remove()

    forms.forEach((form, i) => {
        form.innerHTML.replace(formRegex, `product_line-${i}-`)
        console.log(form)
    })
}

addButton.addEventListener('click', addForm)
deleteButton.addEventListener('click', deleteForm)