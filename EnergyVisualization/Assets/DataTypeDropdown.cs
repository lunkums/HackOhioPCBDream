using TMPro;
using UnityEngine;
using UnityEngine.UI;
using static DataManager;

public class DataTypeDropdown : MonoBehaviour
{
    private DataType[] options;

    private void Awake()
    {
        options = new DataType[]
        { 
            DataType.Total, DataType.Steam, DataType.Electricity,
            DataType.ChilledWater, DataType.HotWater, DataType.NaturalGas
        };
    }

    private void Start()
    {
        TMP_Dropdown dropdown = GetComponent<TMP_Dropdown>();
        dropdown.onValueChanged.AddListener(UpdateDataType);
    }

    private void UpdateDataType(int option)
    {
        DataManager.Instance.CurrentDataType = options[option];
        BuildingManager.Instance.ReadjustBuildings();
    }
}
