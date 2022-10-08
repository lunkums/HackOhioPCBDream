using UnityEngine;

public class Building : MonoBehaviour
{
    [SerializeField] private string _name;

    private Transform building;
    private Material material;

    private void Awake()
    {
        building = transform;
        material = GetComponent<MeshRenderer>().material;
    }

    private void Start()
    {
        Adjust();
    }

    public void Adjust()
    {
        DataManager dm = DataManager.Instance;
        float data = dm.GetData(_name);
        float height = BuildingManager.Instance.MaxBuildingHeight * dm.GetRatio(data);

        material.color = dm.GetColorFromData(data);
        building.localScale = new Vector3(building.localScale.x, height, building.localScale.z);
        building.position = new Vector3(building.position.x, height / 2, building.position.z);
    }
}
